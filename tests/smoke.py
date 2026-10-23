"""Browser checks for the static site; starts its own temporary HTTP server.

python3 tests/smoke.py --artifacts /tmp/gymforce-review
Requires Playwright and Chromium; neither is needed to run the website.
"""
from argparse import ArgumentParser
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import unquote, urlsplit
import json
import shutil

from playwright.sync_api import Error, expect, sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "instalaciones.html", "clases.html", "entrenadores.html", "tarifas.html", "entrenamiento.html", "contacto.html", "legal.html"]


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.references = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            assert attributes["id"] not in self.ids, ("Duplicate ID", attributes["id"])
            self.ids.add(attributes["id"])
        for key in ("href", "src", "srcset"):
            if key in attributes:
                self.references.append(attributes[key])


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def static_checks():
    documents = {name: Document((ROOT / name).read_text()) for name in PAGES}
    for name, document in documents.items():
        for reference in document.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            assert reference != "#", (name, "Empty link")
            target = unquote(url.path) or name
            assert (ROOT / target).is_file(), (name, target)
            if url.fragment:
                assert url.fragment in documents[target].ids, (name, reference)
    print("PASS: local links, assets, anchors and unique IDs")


def main():
    parser = ArgumentParser()
    parser.add_argument("--artifacts", type=Path)
    parser.add_argument("--axe", type=Path, help="Optional local axe.min.js for WCAG checks")
    args = parser.parse_args()
    if args.artifacts:
        args.artifacts.mkdir(parents=True, exist_ok=True)
    static_checks()
    executable = shutil.which("chromium") or shutil.which("google-chrome")
    assert executable, "Install Chromium or Google Chrome for browser checks"
    # Serve under /gymforce/ too, as on the project's GitHub Pages URL.
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT.parent)))
    Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}/{ROOT.name}/"
    errors = []
    requested_urls = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=executable, args=["--no-sandbox"])
            for width, height in [(1440,1000),(1101,900),(1024,768),(768,1024),(760,900),(430,932),(390,844),(375,812),(320,740)]:
                context = browser.new_context(viewport={"width":width,"height":height}, reduced_motion="reduce")
                page = context.new_page()
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.on("request", lambda request: requested_urls.append(request.url))
                for target in PAGES:
                    response = page.goto(base + target)
                    assert response.status == 200
                    page.evaluate("document.fonts.ready")
                    for image in page.locator("img").all():
                        image.scroll_into_view_if_needed()
                        image.evaluate("image => image.decode()")
                    page.evaluate("window.scrollTo(0,0)")
                    metrics = page.evaluate("""() => ({
                        width:innerWidth, scroll:document.documentElement.scrollWidth,
                        overflow:[...document.querySelectorAll('h1,h2,h3,.button')]
                          .filter(e => e.getBoundingClientRect().right > innerWidth+1 || e.scrollWidth > e.clientWidth+2)
                          .map(e => e.outerHTML.slice(0,100))
                    })""")
                    assert metrics["scroll"] == width, (width,target,metrics)
                    assert not metrics["overflow"], (width,target,metrics)
                    expect(page.locator("h1")).to_have_count(1)
                    expect(page.locator(".footer-legal a")).to_have_text([
                        "Aviso legal", "Privacidad", "Cookies", "Condiciones de uso"
                    ])
                    for anchor, section in zip(page.locator(".footer-legal a").all(), ["aviso-legal", "privacidad", "cookies", "condiciones"]):
                        expect(anchor).to_have_attribute("href", f"legal.html#{section}")
                    if args.axe and width in [1440,390]:
                        page.add_script_tag(path=str(args.axe.resolve()))
                        result = page.evaluate("""async () => await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}})""")
                        violations = [{"id":v["id"],"nodes":[n["target"] for n in v["nodes"]]} for v in result["violations"]]
                        assert not violations, (width,target,violations)
                    if args.artifacts and width in [1440,390]:
                        device = "ordenador" if width == 1440 else "movil"
                        stem = "inicio" if target == "index.html" else target.removesuffix(".html")
                        page.screenshot(path=str(args.artifacts / f"{stem}-{device}.png"), full_page=True)
                        if target == "index.html":
                            page.screenshot(path=str(args.artifacts / f"portada-{device}.png"))
                    print(f"PASS: {target} at {width}px — layout, images, title" + (", axe" if args.axe and width in [1440,390] else ""))
                context.close()

            page = browser.new_page(viewport={"width":390,"height":844}, reduced_motion="reduce")
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(base)
            toggle = page.locator(".menu-toggle")
            toggle.click()
            expect(toggle).to_have_attribute("aria-expanded", "true")
            page.keyboard.press("Escape")
            expect(toggle).to_have_attribute("aria-expanded", "false")
            expect(toggle).to_be_focused()
            toggle.click()
            page.locator(".main-nav").get_by_role("link", name="Clases", exact=True).click()
            expect(toggle).to_have_attribute("aria-expanded", "false")
            assert page.evaluate("!document.body.classList.contains('menu-open')")
            print("PASS: mobile menu, Escape, focus restoration and navigation")
            page.goto(base)
            for category, count in [("strength",2),("cardio",3),("balance",1),("all",6)]:
                page.locator(f'[data-class-filter="{category}"]').click()
                expect(page.locator(".class-card:visible")).to_have_count(count)
                expect(page.locator(f'[data-class-filter="{category}"]')).to_have_attribute("aria-pressed", "true")
            print("PASS: all four class filters and their results")
            for plan in ["mensual","trimestral","anual"]:
                page.goto(base + "tarifas.html")
                page.get_by_role("link", name=f"Elegir {plan}").click()
                expect(page.locator("#interes")).to_have_value(plan)
            print("PASS: all three plans preselect the contact option")
            page.locator("#nombre").fill("Persona de prueba")
            page.locator("#correo").fill("incorrecto")
            page.get_by_role("button",name="Probar formulario").click()
            expect(page.locator("#form-feedback")).to_be_empty()
            assert not page.locator("#correo").evaluate("e => e.validity.valid")
            page.locator("#correo").fill("prueba@example.com")
            page.locator("#nombre").fill("   ")
            page.get_by_role("button",name="Probar formulario").click()
            expect(page.locator("#form-feedback")).to_be_empty()
            page.locator("#nombre").fill("Persona de prueba")
            requests = []
            page.on("request",lambda request:requests.append(request.url))
            page.get_by_role("button",name="Probar formulario").click()
            expect(page.locator("#form-feedback")).to_contain_text("No se ha enviado")
            assert not requests, requests
            assert page.evaluate("localStorage.length === 0 && sessionStorage.length === 0 && document.cookie === ''")
            print("PASS: invalid data blocked; valid demo makes no requests and stores no data")
            page.goto(base + "tarifas.html")
            page.locator(".faq-list summary").first.click()
            expect(page.locator(".faq-list details").first).to_have_attribute("open", "")
            print("PASS: FAQ disclosure")
            page.goto(base + "clases.html")
            expect(page.locator(".class-card")).to_have_count(7)
            page.locator('[data-class-filter="cardio"]').click()
            expect(page.locator(".class-card:visible")).to_have_count(4)
            page.locator('[data-class-filter="balance"]').click()
            page.get_by_role("link",name="Consultar sobre Yoga Reset").click()
            expect(page.locator("#interes")).to_have_value("clases")
            expect(page.locator("#mensaje")).to_have_value("Me gustaría conocer más sobre Yoga Reset.")
            print("PASS: extended class catalogue and enquiry context")
            for index, coach in enumerate(["Sofía", "Deiby", "Alex"]):
                page.goto(base + "entrenadores.html")
                expect(page.locator(".coach-copy h3")).to_have_text(["Sofía", "Deiby", "Alex"])
                expect(page.locator(".photo-placeholder-label:visible")).to_have_count(0)
                page.get_by_role("link",name="Consultar entrenamiento").nth(index).click()
                expect(page.locator("#mensaje")).to_have_value(f"Me gustaría consultar sobre entrenamiento con {coach}.")
            page.goto(base)
            expect(page.locator(".coach-copy h3")).to_have_text(["Sofía", "Deiby", "Alex"])
            expect(page.locator(".photo-placeholder-label:visible")).to_have_count(0)
            assert page.locator('.hero-picture img').get_attribute("src") == "img/gym-force-hero.webp"
            expect(page.locator(".space-photo .image-tag")).to_have_text("Imagen conceptual")
            expect(page.locator('.hero-picture [data-photo-slot="alex"]')).to_have_count(0)
            expect(page.locator('.space-photo [data-photo-slot="alex-entrenamiento"]')).to_have_count(0)
            for target in ['index.html', 'entrenadores.html']:
                page.goto(base + target)
                expect(page.locator('.founder-section')).to_have_count(1)
                expect(page.locator('.founder-role')).to_have_text('Fundador y Director de Gym Force')
                expect(page.locator('.coach-grid [data-photo-slot="alvaro"]')).to_have_count(0)
                expect(page.locator('.coach-grid .coach-card')).to_have_count(3)
                assert page.locator('.founder-section').evaluate('el => !!(el.compareDocumentPosition(document.querySelector(".coach-grid")) & Node.DOCUMENT_POSITION_FOLLOWING)')
                for slot in ['alvaro','sofia','deiby','alex']:
                    portrait = page.locator(f'[data-photo-slot="{slot}"]')
                    expect(portrait).to_have_attribute('src', f'img/personas/{slot}.webp')
                    portrait.scroll_into_view_if_needed()
                    portrait.evaluate('image => image.decode()')
                    assert portrait.evaluate('image => image.naturalHeight > image.naturalWidth')
                    assert portrait.locator('..').get_attribute('data-placeholder-panel') is None
            page.goto(base + "contacto.html")
            expect(page.locator(".contact-details")).to_contain_text("Avenida del Sur")
            expect(page.locator(".contact-details")).to_contain_text("Valdepeñas, Ciudad Real, España")
            assert "Madrid" not in page.locator(".contact-details").inner_text()
            page.goto(base + "contacto.html?entrenador=%C3%81lvaro#contacto")
            expect(page.locator('#mensaje')).to_have_value('')
            page.goto(base + 'clases.html')
            assert not page.locator('.class-schedule dd').filter(has_text='Álvaro').count()
            print("PASS: founder before three trainers, four portraits, new enquiries, founder excluded from classes, unchanged hero and fictional location")
            page.goto(base + "entrenamiento.html")
            expect(page.locator(".exercise-card:visible")).to_have_count(14)
            for group in ["pecho","espalda","piernas","hombros","biceps","triceps","core"]:
                page.locator(f'[data-exercise-filter="{group}"]').click()
                expect(page.locator(".exercise-card:visible")).to_have_count(2)
            page.locator('[data-exercise-filter="all"]').click()
            page.locator("#exercise-search").fill("biceps")
            expect(page.locator(".exercise-card:visible")).to_have_count(2)
            page.locator("#exercise-search").fill("sentadilla")
            expect(page.locator(".exercise-card:visible")).to_have_count(1)
            page.locator('[data-exercise-filter="pecho"]').click()
            expect(page.locator("#exercise-empty")).to_be_visible()
            expect(page.locator(".exercise-card:visible")).to_have_count(0)
            page.get_by_role("button",name="Mostrar todos los ejercicios").click()
            expect(page.locator(".exercise-card:visible")).to_have_count(14)
            expect(page.locator("#exercise-search")).to_be_focused()
            page.locator(".exercise-card summary").first.click()
            expect(page.locator(".exercise-card details").first).to_have_attribute("open", "")
            print("PASS: 7 muscle filters, accent-insensitive search, combined filters, empty/reset state and technique")
            page.close()

            # Verify both forms from a fresh context, including typing and validation.
            context = browser.new_context(viewport={"width":390,"height":844}, reduced_motion="reduce")
            page = context.new_page()
            page.on("pageerror", lambda error: errors.append(str(error)))
            for target in ["index.html", "contacto.html"]:
                page.goto(base + target)
                for image in page.locator("img").all():
                    image.scroll_into_view_if_needed()
                    image.evaluate("image => image.decode()")
                page.wait_for_load_state("networkidle")
                form_requests = []
                def record_request(request):
                    form_requests.append(request.url)
                page.on("request", record_request)
                expect(page.locator("#contact-form [name]")).to_have_count(0)
                page.locator("#nombre").fill("Prueba ficticia legal")
                page.locator("#correo").fill("prueba@example.com")
                page.locator("#mensaje").fill("Mensaje ficticio de revisión")
                page.get_by_role("button", name="Probar formulario").click()
                expect(page.locator("#form-feedback")).to_contain_text("No se ha enviado")
                page.wait_for_timeout(200)
                assert not form_requests, (target, form_requests)
                page.remove_listener("request", record_request)
                assert page.url == base + target
                assert not context.cookies()
                assert page.evaluate("localStorage.length === 0 && sessionStorage.length === 0")
                assert page.evaluate("async () => (await indexedDB.databases()).length === 0")
                assert page.evaluate("async () => (await navigator.serviceWorker.getRegistrations()).length === 0")
            print("PASS: both demo forms send no requests during input/submission, retain no application storage and do not put field contents in URLs")
            page.goto(base + "legal.html")
            expect(page.locator(".legal-section")).to_have_count(4)
            for section in ["aviso-legal", "privacidad", "cookies", "condiciones"]:
                page.locator(f'.legal-toc a[href="#{section}"]').click()
                expect(page).to_have_url(base + "legal.html#" + section)
                heading = page.locator(f"#{section} h2")
                expect(heading).to_be_in_viewport()
                assert heading.bounding_box()["y"] >= page.locator(".site-header").bounding_box()["height"]
            assert all(url.startswith(base) for url in requested_urls), requested_urls
            print("PASS: four legal anchors work on mobile below the header; no third-party resource requests on the eight pages")
            context.close()

            context = browser.new_context(java_script_enabled=False,viewport={"width":390,"height":844})
            page = context.new_page()
            page.goto(base)
            expect(page.locator('.main-nav a[href="clases.html"]')).to_be_visible()
            expect(page.locator(".class-card")).to_have_count(6)
            expect(page.locator(".form-submit")).to_be_disabled()
            print("PASS: navigation and content without JavaScript; demo cannot submit")
            context.close()

            context = browser.new_context(offline=True, reduced_motion="reduce")
            page = context.new_page()
            try:
                page.goto((ROOT / "tarifas.html").as_uri())
            except Error as error:
                if "ERR_BLOCKED_BY_ADMINISTRATOR" not in str(error):
                    raise
                print("BLOCKED: file:// offline check — this managed browser forbids local file URLs; no website failure inferred")
            else:
                page.get_by_role("link",name="Elegir anual").click()
                expect(page.locator("#interes")).to_have_value("anual")
                page.locator('[data-class-filter="balance"]').click()
                expect(page.locator(".class-card:visible")).to_have_count(1)
                assert page.locator(".hero-picture img").evaluate("e => e.complete && e.naturalWidth > 0")
                print("PASS: downloaded site works offline via file://, including scripts and images")
            context.close()
            browser.close()
            assert not errors, errors
            print("PASS: no uncaught JavaScript errors")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()

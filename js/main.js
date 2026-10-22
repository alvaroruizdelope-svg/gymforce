/* Progressive enhancement. Public pages also work by opening index.html. */
document.documentElement.classList.add("js");

const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#navegacion");
if (menuToggle && navigation) {
  const closeMenu = (restoreFocus = false) => {
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.querySelector(".menu-label").textContent = "Menú";
    navigation.classList.remove("is-open");
    document.body.classList.remove("menu-open");
    if (restoreFocus) menuToggle.focus();
  };
  menuToggle.addEventListener("click", () => {
    const open = menuToggle.getAttribute("aria-expanded") !== "true";
    menuToggle.setAttribute("aria-expanded", String(open));
    menuToggle.querySelector(".menu-label").textContent = open
      ? "Cerrar"
      : "Menú";
    navigation.classList.toggle("is-open", open);
    document.body.classList.toggle("menu-open", open);
  });
  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });
  document.addEventListener("keydown", (event) => {
    if (
      event.key === "Escape" &&
      menuToggle.getAttribute("aria-expanded") === "true"
    )
      closeMenu(true);
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".site-header")) closeMenu();
  });
  document.addEventListener("focusin", (event) => {
    if (!event.target.closest(".site-header")) closeMenu();
  });
  window
    .matchMedia("(min-width: 1101px)")
    .addEventListener("change", (event) => {
      if (event.matches) closeMenu();
    });
}

const classFilters = document.querySelectorAll("[data-class-filter]");
const classCards = document.querySelectorAll("[data-class-category]");
classFilters.forEach((button) => {
  button.addEventListener("click", () => {
    const category = button.dataset.classFilter;
    let visible = 0;
    classCards.forEach((card) => {
      card.hidden =
        category !== "all" && card.dataset.classCategory !== category;
      if (!card.hidden) visible += 1;
    });
    classFilters.forEach((filter) => {
      const active = filter === button;
      filter.classList.toggle("is-active", active);
      filter.setAttribute("aria-pressed", String(active));
    });
    document.querySelector("#class-status").textContent =
      `${visible} ${visible === 1 ? "clase disponible" : "clases disponibles"}.`;
  });
});

const contactForm = document.querySelector("#contact-form");
if (contactForm) {
  const parameters = new URLSearchParams(window.location.search);
  const selectedPlan = parameters.get("plan");
  const interest = contactForm.querySelector("#interes");
  if (["mensual", "trimestral", "anual"].includes(selectedPlan))
    interest.value = selectedPlan;
  const requestedClass = parameters.get("clase");
  const requestedCoach = parameters.get("entrenador");
  const allowedClasses = [
    "Functional Force",
    "HIIT The Limit",
    "Yoga Reset",
    "Ride Together",
    "Body Power",
    "Boxing Energy",
    "Dance Force",
  ];
  const allowedCoaches = ["Sofía", "Deiby", "Alex"];
  if (allowedClasses.includes(requestedClass)) {
    interest.value = "clases";
    contactForm.querySelector("#mensaje").value =
      `Me gustaría conocer más sobre ${requestedClass}.`;
  } else if (allowedCoaches.includes(requestedCoach)) {
    contactForm.querySelector("#mensaje").value =
      `Me gustaría consultar sobre entrenamiento con ${requestedCoach}.`;
  }
  const feedback = document.querySelector("#form-feedback");
  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!contactForm.reportValidity()) return;
    const name = contactForm.querySelector("#nombre");
    if (!name.value.trim()) {
      name.setCustomValidity(
        "Escribe un nombre que no esté formado solo por espacios.",
      );
      name.reportValidity();
      return;
    }
    // Demonstration: no request, analytics, localStorage or persistence.
    feedback.textContent =
      "¡Todo correcto! Has completado la demostración. No se ha enviado ningún mensaje ni guardado tus datos.";
  });
  contactForm.addEventListener("input", () => {
    contactForm.querySelector("#nombre").setCustomValidity("");
    feedback.textContent = "";
  });
  contactForm.querySelector('[type="submit"]').disabled = false;
}

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = new Date().getFullYear();
});

if (
  "IntersectionObserver" in window &&
  !window.matchMedia("(prefers-reduced-motion: reduce)").matches
) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal-in");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 },
  );
  document
    .querySelectorAll(
      ".section-heading, .intro-grid, .values-row, .class-card, .pricing-card, .contact-grid",
    )
    .forEach((element) => observer.observe(element));
}

// Search and group selection compose; accents do not affect search results.
const exerciseCards = [...document.querySelectorAll("[data-muscle]")];
const exerciseFilters = document.querySelectorAll("[data-exercise-filter]");
const exerciseSearch = document.querySelector("#exercise-search");
if (exerciseSearch && exerciseCards.length) {
  let group = "all";
  const normalize = (value) =>
    value
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .trim();
  const filterExercises = () => {
    const query = normalize(exerciseSearch.value);
    let count = 0;
    exerciseCards.forEach((card) => {
      const matchesGroup = group === "all" || card.dataset.muscle === group;
      const matchesQuery = normalize(card.dataset.search).includes(query);
      card.hidden = !(matchesGroup && matchesQuery);
      if (!card.hidden) count += 1;
    });
    document.querySelector("#exercise-status").textContent =
      `${count} ${count === 1 ? "ejercicio disponible" : "ejercicios disponibles"}.`;
    document.querySelector("#exercise-empty").hidden = count !== 0;
    exerciseFilters.forEach((button) => {
      const active = button.dataset.exerciseFilter === group;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
  };
  exerciseFilters.forEach((button) =>
    button.addEventListener("click", () => {
      group = button.dataset.exerciseFilter;
      filterExercises();
    }),
  );
  exerciseSearch.addEventListener("input", filterExercises);
  document.querySelector("#exercise-reset").addEventListener("click", () => {
    group = "all";
    exerciseSearch.value = "";
    filterExercises();
    exerciseSearch.focus();
  });
}

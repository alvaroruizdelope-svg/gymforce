# GYM FORCE

Web de portfolio de un gimnasio ficticio, diseñada y desarrollada por Álvaro. HTML5, CSS y JavaScript sin frameworks, instalación ni proceso de compilación.

La parte pública incluye portada, instalaciones, clases, entrenadores, tarifas, biblioteca de ejercicios, contacto e información legal. Se conserva la identidad negro, blanco y amarillo y los precios originales de los tres planes.

## Ver y desarrollar

Abre `index.html` en el navegador. Todos los recursos se incluyen en el proyecto y las rutas son relativas; está preparado para abrirse sin conexión después de descargarlo y descomprimirlo. En el navegador administrado de este entorno, la política bloquea las direcciones `file://`, por lo que aquí la validación funcional se realizó por HTTP local.

Para desarrollo con un servidor estático, desde la carpeta del proyecto:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

El proyecto es compatible con alojamiento estático como GitHub Pages desde la raíz. Esta entrega no activa GitHub Pages ni configura un dominio. No necesita claves, servicios externos ni una base de datos.

## Estructura

- `index.html`: portada, presentación, instalaciones y clases destacadas, equipo, entrenamiento, tarifas y contacto.
- `instalaciones.html`: seis zonas del gimnasio conceptual.
- `clases.html`: siete actividades con filtros, duración, intensidad y horarios de ejemplo.
- `entrenadores.html`: tres perfiles ficticios con consultas contextualizadas.
- `tarifas.html`: mensual, trimestral y anual; selección de plan y preguntas frecuentes.
- `entrenamiento.html`: 14 ejercicios de siete grupos musculares, búsqueda y técnica básica.
- `contacto.html`: formulario y datos de ejemplo, sin dirección o contactos operativos.
- `legal.html`: carácter demostrativo, privacidad y procedencia de recursos.
- `css/estilos.css`: diseño compartido, componentes y adaptación responsive.
- `js/main.js`: menú, filtros, búsqueda, contexto de consultas y formulario demostrativo.
- `img/`: fotografías conceptuales optimizadas en WebP y favicon SVG.
- `fonts/`: Barlow Condensed 700/800, alojada localmente con su licencia OFL.
- `tests/smoke.py`: comprobaciones de navegador, enlaces y funcionamiento sin conexión.
- `docs/`: auditoría inicial, alcance y evolución futura.

Las cabeceras y pies están en cada HTML para que la navegación esté disponible sin JavaScript y al abrir los archivos directamente. Mantén sus enlaces sincronizados al incorporar nuevas páginas; no hay plantillas ni un generador necesarios para servir la web.

## Interacciones

El menú compacto funciona en móvil y tablet, se cierra con Escape y devuelve el foco al botón. Los filtros de clases indican su selección y anuncian el número de resultados. La biblioteca permite combinar búsquedas sin distinguir tildes con filtros musculares y ofrece una acción para recuperar todos los resultados.

Los planes abren el contacto de la portada con el plan elegido. Las consultas desde clases o entrenadores abren la página de contacto con el motivo preparado. El formulario usa validación nativa y rechaza nombres formados solo por espacios. Su confirmación explica que no se ha enviado ni guardado información. Con JavaScript desactivado, la navegación y los contenidos siguen disponibles y el envío permanece deshabilitado.

Los efectos respetan `prefers-reduced-motion`. Las imágenes bajo el primer bloque usan carga diferida; el hero tiene una versión más ligera para móviles. No hay fuentes, analítica, mapas ni imágenes que requieran proveedores externos durante la navegación.

## Validación de desarrollo

Estas herramientas solo son necesarias para las pruebas, no para visitar o publicar la web. El entorno utilizado ya incluye Python, Playwright y Chromium.

```sh
python3 -m pip install playwright==1.62.0
python3 tests/smoke.py --artifacts /tmp/gymforce-review
```

El sistema debe disponer de `chromium` o `google-chrome`. El script levanta un servidor temporal y lo cierra al terminar. Comprueba las ocho páginas en nueve anchuras, rutas e imágenes, el menú móvil, los filtros, los tres planes, la validación, la ausencia de envío y almacenamiento del formulario, las consultas y el uso sin JavaScript y, cuando el navegador lo permite, mediante `file://` sin conexión. Si una política del navegador impide esta última comprobación, se registra como `BLOCKED`, sin marcarla como aprobada.

Para añadir una revisión automática WCAG A/AA con axe-core, se puede indicar una copia local de `axe.min.js`:

```sh
python3 tests/smoke.py --axe /ruta/a/axe.min.js
```

Esta revisión automática complementa las comprobaciones visuales; no sustituye una auditoría completa de accesibilidad ni pruebas físicas en todos los dispositivos.

## Contenido de demostración

No existe un gimnasio operativo detrás de esta web. Las instalaciones, horarios y ofertas son ficticios. Los perfiles se preparan para Álvaro, Sofía y Deiby, con especialidades y biografías provisionales de demostración; la fotografía de Álvaro es la aportada por el usuario con fondo editado y las imágenes provisionales de Sofía y Deiby no las representan. Las demás fotografías se han generado para el concepto; los esquemas musculares SVG son ilustrativos. Las fuentes se distribuyen con su licencia en `fonts/Barlow-Condensed-LICENSE.txt`.

El formulario no transmite datos, no hay pagos ni altas reales y no se utilizan cookies ni almacenamiento web. El alojamiento puede tener sus propios registros técnicos. Registro, acceso, reservas, área de socio y administración pertenecen a una fase posterior; consulta `docs/EVOLUCION.md`.

## Fotografías personales pendientes

Están preparados los tres perfiles de Álvaro, Sofía y Deiby en Inicio y Entrenadores, sus consultas y sus referencias en Clases. La ubicación ficticia del concepto es Avenida del Sur, Valdepeñas, Ciudad Real, España, sin número de portal ni sede operativa.

La fotografía de Álvaro ya está integrada en Inicio y Entrenadores con su fondo editado y optimizada en WebP. Quedan por recibir Sofía, Deiby y Alex. Según la aclaración del usuario, Alex sustituirá al hombre del hero de la portada principal, no a THE TRAINING FLOOR. Los destinos y el estado están documentados en `img/personas/README.md`. No se prepara la entrega definitiva hasta recibir e integrar las cuatro fotografías.

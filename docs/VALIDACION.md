# Validación de la entrega

Realizada el 22 de octubre de 2026 sobre la implementación pública de esta entrega.

- Ocho páginas comprobadas en Chromium a 1440, 1101, 1024, 768, 760, 430, 390, 375 y 320 píxeles: 72 combinaciones. Sin desbordamiento horizontal o texto recortado detectado en los títulos y botones; imágenes cargadas y un título principal por página.
- 16 revisiones automáticas axe-core 4.10.3: ocho páginas a 1440 y 390 píxeles, con reglas WCAG A/AA y WCAG 2.1 AA. Sin infracciones detectadas por ese conjunto de reglas.
- Rutas locales, recursos, anclas e identificadores comprobados.
- Menú móvil, cierre mediante Escape, devolución del foco y navegación comprobados.
- Filtros de clases en la portada y catálogo completo comprobados.
- Los tres planes preseleccionan su opción de contacto.
- Datos de formulario incorrectos rechazados; confirmación válida sin nuevas peticiones ni uso de cookies, localStorage o sessionStorage por la aplicación.
- Consultas de clases y entrenadores conservan su contexto.
- Siete filtros musculares, búsqueda sin distinguir tildes, combinación de filtro y búsqueda, estado vacío, reinicio y despliegue de técnica comprobados.
- Navegación y contenidos disponibles con JavaScript desactivado; formulario deshabilitado.
- Sin excepciones JavaScript detectadas en los recorridos de prueba. Sintaxis de `js/main.js` y `git diff --check` correctos.

## Limitaciones de la validación

La política del Chromium administrado bloquea `file://` con `ERR_BLOCKED_BY_ADMINISTRATOR`. La comprobación directa del ZIP sin conexión se registra como **BLOCKED**, no como aprobada. El proyecto usa archivos y rutas relativas y no necesita un servidor de aplicación; sus recorridos se validaron por HTTP local. No se ha modificado la política del navegador para evitar ese bloqueo.

No se han realizado pruebas en dispositivos físicos, Safari o Firefox, ni una auditoría manual completa con tecnologías de asistencia. Las revisiones automáticas no garantizan por sí solas conformidad total de accesibilidad.

La aplicación no se ha publicado en GitHub Pages. Tras completar esta validación, la versión se entregó en la rama `gymforce-vista-previa`, con autorización del usuario y sin modificar `main`. Cuentas, reservas, pagos y backend quedan fuera de esta fase pública.

## Reproducir

Desde la raíz del repositorio, con Playwright y Chromium disponibles:

```sh
python3 tests/smoke.py --artifacts /tmp/gymforce-review --axe /ruta/a/axe.min.js
```

El parámetro `--axe` es opcional. El script informa por separado de resultados aprobados y de la comprobación de archivos bloqueada por la política del navegador.

## Actualización de perfiles y fotografías pendientes

Se repitieron las 72 combinaciones de página y anchura y las 16 revisiones axe después de preparar Álvaro, Sofía y Deiby. Las pruebas comprueban los tres perfiles en Inicio y Entrenadores, sus tres consultas contextualizadas, las etiquetas provisionales, la foto existente de THE TRAINING FLOOR y la nueva ubicación ficticia en Valdepeñas. Todas esas comprobaciones pasaron. La restricción conocida de `file://` se mantiene y se informa por separado.

No se ha alterado ningún archivo de imagen provisional. La carpeta `img/personas/` documenta los cuatro destinos definitivos, pero las fotos reales aún no se han recibido ni integrado. La sustitución de las cuatro fotografías sigue pendiente.

## Integración parcial de Álvaro

Recibida la fotografía identificada por el usuario como Álvaro, se ha preparado su fondo de gimnasio y se ha integrado la imagen optimizada en las tarjetas de Inicio y Entrenadores. Se comprobaron de nuevo las ocho páginas en nueve anchuras y las 16 revisiones axe, así como la carga del retrato vertical en ambos lugares, las otras dos etiquetas provisionales y las consultas de los tres perfiles. La restricción de `file://` continúa informada por separado.

También se corrigió el destino de Alex conforme a la aclaración del usuario: su foto irá en el hero principal de Inicio y su variante móvil, no en THE TRAINING FLOOR. La foto de esa sección permanece intacta. Sofía, Deiby y Alex siguen pendientes de recepción. No se ha preparado un ZIP definitivo ni se ha publicado la integración parcial.

## Integración parcial de Sofía

La fotografía aportada como Sofía se ha editado para sustituir el fondo por un gimnasio y se ha integrado en Inicio y Entrenadores, conservando la camiseta y el logotipo del original como referencia de la edición. Se ha optimizado a WebP y se ha ajustado el encuadre superior para dejar visible la cabeza en las tarjetas.

La revisión específica comprueba ambas páginas a 1440, 1024, 768, 390 y 320 píxeles (10 vistas), los dos retratos reales de Álvaro y Sofía, la única etiqueta provisional de Deiby, las rutas locales y la ausencia de desbordamientos y excepciones JavaScript. Se ejecutan cuatro auditorías axe en las vistas de escritorio y móvil. Quedan pendientes las fotos de Deiby y Alex; todavía no se prepara ni se publica la entrega definitiva.

## Integración parcial de Deiby

El usuario confirmó que la tercera fotografía corresponde a Deiby. Se preparó el fondo de gimnasio y se integró la imagen WebP en sus dos tarjetas, manteniendo el margen superior de la cabeza y retirando la última etiqueta de fotografía provisional del equipo.

La revisión específica de Inicio y Entrenadores pasó en cinco anchuras por página: 10 vistas y cuatro auditorías axe, sin desbordamientos ni excepciones JavaScript. Se verificó la carga de los tres retratos reales, sus proporciones verticales y la ausencia de recortes temporales de tres paneles. La entrega definitiva sigue pendiente únicamente de Alex para el hero de Inicio; no se ha publicado esta integración parcial ni preparado todavía el ZIP definitivo.

## Entrega de revisión con los tres retratos

El usuario solicitó recibir los archivos actuales antes de enviar la última fotografía. Se entrega esta versión por la rama `gymforce-vista-previa`, con los retratos de Álvaro, Sofía y Deiby integrados y ya comprobados. No se activa GitHub Pages ni se modifica `main`. La imagen provisional del hero y su variante móvil se conservan hasta recibir la foto de Alex. La descarga se comprueba como ZIP completo, incluyendo los tres archivos WebP y sus referencias en las dos páginas.

## Sustitución del retrato de Álvaro

Se reemplaza el primer retrato por la nueva fotografía aportada por el usuario, con el logotipo Gym Force en la sudadera. Se edita su fondo y se actualizan el WebP, las dimensiones y el encuadre en Inicio y Entrenadores. Las imágenes de Sofía, Deiby y la portada provisional no se modifican.

La revisión específica pasó en las dos páginas y cinco anchuras (10 vistas), con cuatro auditorías axe, carga correcta de los tres retratos y ausencia de desbordamientos y excepciones JavaScript. Se entrega un ZIP de revisión actualizado; Alex continúa pendiente para la portada principal.

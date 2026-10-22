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

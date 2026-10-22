# Fotografías reales pendientes

No se han recibido ni incorporado las cuatro fotografías. No hay imágenes inventadas de Álvaro, Sofía, Deiby o Alex. La web sigue utilizando sus imágenes provisionales existentes, identificadas como tales.

| Archivo final previsto    | Uso                                         | Provisional activo                 |
| ------------------------- | ------------------------------------------- | ---------------------------------- |
| `alvaro.webp`             | Tarjetas de Álvaro en Inicio y Entrenadores | Primer panel de `../coaches.webp`  |
| `sofia.webp`              | Tarjetas de Sofía en Inicio y Entrenadores  | Segundo panel de `../coaches.webp` |
| `deiby.webp`              | Tarjetas de Deiby en Inicio y Entrenadores  | Tercer panel de `../coaches.webp`  |
| `alex-entrenamiento.webp` | THE TRAINING FLOOR en Inicio                | `../gym-force-hero.webp`           |

Los atributos `data-photo-slot` identifican las cuatro posiciones y `data-photo-target` indican el archivo definitivo previsto. Son metadatos, no peticiones a archivos que aún no existen. No se debe cambiar `src` hasta disponer de una fotografía optimizada y validada.

Cuando se reciban las fotografías:

1. Conservar los originales y los rostros. Editar los fondos solo según lo solicitado por el usuario, sin inventar rasgos físicos.
2. Optimizar las imágenes en WebP y guardar aquí los cuatro archivos reales. Los retratos deben ser verticales, con margen sobre la cabeza; la foto de entrenamiento, horizontal.
3. En ambos lugares de cada entrenador, cambiar `src`, dimensiones intrínsecas y texto alternativo a la foto real. Quitar `data-placeholder-panel` del contenedor. El retrato pasará del recorte temporal de tres paneles a una imagen independiente al 100%, sin deformación. Ajustar `--portrait-position` solo si el encuadre lo requiere.
4. En THE TRAINING FLOOR, cambiar únicamente la imagen de esa sección; no el hero ni otras imágenes reutilizadas. Quitar `data-photo-placeholder` del contenedor: la etiqueta «Imagen conceptual» dejará de mostrarse. Ajustar `--training-photo-position` para cada pantalla si es necesario.
5. Actualizar las notas provisionales y la información legal según las fotografías efectivamente recibidas. No presentar como definitivas las biografías o especialidades pendientes de confirmar.
6. Comprobar rostros y encuadres en móvil, tablet y escritorio, proporciones sin estiramiento, carga de imágenes, tarjetas equilibradas y ausencia de desbordamiento. Actualizar las pruebas que describen el estado provisional.

La estructura está preparada, pero la sustitución de fotografías no está completada.

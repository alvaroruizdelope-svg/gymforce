# Fotografías del proyecto: integración parcial

Las fotos identificadas por el usuario como Álvaro, Sofía y Deiby están recibidas e integradas en Inicio y Entrenadores. Se han sustituido sus fondos por un gimnasio siguiendo las instrucciones de conservar su aspecto, ropa y postura. Los resultados se optimizan en `alvaro.webp`, `sofia.webp` y `deiby.webp`; las salidas de edición PNG se conservan fuera del checkout. Las fotografías originales siguen en la conversación aportadas por el usuario.

Alex sigue pendiente. La imagen anterior del hero se conserva y no se ha generado una persona nueva para sustituirlo. El ZIP definitivo se entregará cuando estén las cuatro fotografías integradas y comprobadas.

| Archivo                          | Uso                                         | Estado                                     |
| -------------------------------- | ------------------------------------------- | ------------------------------------------ |
| `alvaro.webp`                    | Tarjetas de Álvaro en Inicio y Entrenadores | Recibida, fondo editado e integrada        |
| `sofia.webp`                     | Tarjetas de Sofía en Inicio y Entrenadores  | Recibida, fondo editado e integrada        |
| `deiby.webp`                     | Tarjetas de Deiby en Inicio y Entrenadores  | Recibida, fondo editado e integrada        |
| `alex-entrenamiento.webp`        | Hero de la portada principal de Inicio      | Pendiente; `../gym-force-hero.webp`        |
| `alex-entrenamiento-mobile.webp` | Variante optimizada del mismo hero en móvil | Pendiente; `../gym-force-hero-mobile.webp` |

## Corrección de destino de Alex

El usuario aclaró que Alex sustituirá al hombre del inicio de la página, en `.hero-picture`. No sustituye la foto de la sección THE TRAINING FLOOR. El hero, su variante móvil y su precarga deben actualizarse juntos al recibir la fotografía; THE TRAINING FLOOR y sus etiquetas se conservan.

## Incorporación de las siguientes fotos

Los atributos `data-photo-slot` identifican las posiciones y `data-photo-target` indican sus archivos. Estos metadatos no descargan imágenes que aún no existen.

1. Conservar los originales y los rostros. Editar únicamente los fondos según lo solicitado, sin inventar rasgos físicos ni cambiar ropa, postura o complexión.
2. Optimizar en WebP y guardar aquí las fotografías reales. Los retratos deben ser verticales y dejar margen sobre la cabeza; la foto de Alex debe permitir un hero horizontal con espacio para el texto a la izquierda.
3. En ambas tarjetas de cada entrenador, cambiar `src`, dimensiones intrínsecas y texto alternativo. Quitar `data-placeholder-panel` del contenedor y su etiqueta «Fotografía provisional». La imagen real se muestra al 100%, con `object-fit: cover`. Ajustar `--portrait-position` por fotografía cuando haga falta. Álvaro utiliza `center 24%`; Sofía y Deiby, `center top`.
4. Para Alex, actualizar `src` del hero, `srcset` móvil y la precarga correspondiente. Quitar `data-photo-placeholder` de `.hero-picture` cuando la foto real esté integrada. No tocar la imagen ni la etiqueta de THE TRAINING FLOOR.
5. Actualizar las notas de integración y procedencia de las imágenes. Las biografías y especialidades siguen siendo provisionales hasta confirmación del usuario.
6. Comprobar rostros, encuadre, proporciones, carga y tarjetas equilibradas en móvil, tablet y escritorio; actualizar las pruebas de las imágenes pendientes.

La integración total continúa pendiente de la fotografía de Alex. Todavía no se publica ni se entrega un ZIP definitivo.

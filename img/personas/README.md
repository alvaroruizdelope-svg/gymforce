# Fotografías y funciones del equipo

Las cuatro fotos están recibidas e integradas con fondos de gimnasio editados. Las salidas PNG se conservan fuera del checkout y los archivos de la web están optimizados en WebP. Se han usado como referencia las imágenes originales aportadas por el usuario, sin solicitar cambios de rostros, complexión, ropa, joyas ni postura.

| Archivo       | Uso actual                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `alvaro.webp` | Fundador y Director de Gym Force; bloque destacado anterior a entrenadores en Inicio y Entrenadores. Última foto con sudadera negra y logo. |
| `sofia.webp`  | Primera tarjeta de entrenadores en ambas páginas; fotografía conservada.                                                                    |
| `deiby.webp`  | Segunda tarjeta de entrenadores en ambas páginas; fotografía conservada.                                                                    |
| `alex.webp`   | Tercera tarjeta de entrenadores en ambas páginas; Fuerza funcional y técnica.                                                               |

## Decisión sobre la portada

La última indicación del usuario sustituye el plan anterior de usar Alex en el hero: **mantener por ahora la portada actual y usar esta foto de Alex solo como entrenador**. Por tanto, `.hero-picture` conserva `../gym-force-hero.webp` y su variante móvil original. THE TRAINING FLOOR tampoco cambia. No hay una foto de portada pendiente que bloquee esta entrega.

## Encuadres

Los cuatro archivos son retratos verticales. Los tres entrenadores utilizan el mismo contenedor responsive y `object-fit: cover` con posición superior. Álvaro tiene un bloque independiente de presentación, con proporción 4:5 para dar mayor presencia a su fotografía y mostrar el logotipo de la sudadera.

Se conservan los metadatos `data-photo-slot` y `data-photo-target` para reconocer los archivos en el HTML. Las biografías, especialidades y cargos describen el concepto de gimnasio ficticio y no acreditan titulaciones profesionales. Los nombres, fotos y consultas deben mantenerse coherentes entre Inicio, Entrenadores, Clases y el formulario.

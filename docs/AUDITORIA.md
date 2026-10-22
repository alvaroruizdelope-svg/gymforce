# Auditoría inicial y alcance

## Estado de partida

La revisión se realizó sobre el commit `25f9113a0c342d7d7edce9bcfa8eb51ced46363c` de `main`, con el árbol de trabajo limpio. Existían `index.html`, `tarifas.html` y `css/estilos.css`; no había JavaScript, documentación, pruebas, paquetes ni instrucciones de agentes adicionales.

- Ambas páginas empleaban XHTML 1.0 Strict y carecían de `meta viewport` y descripción.
- La portada contenía únicamente cabecera, titular, descripción y enlace a las tarifas.
- La página de tarifas tenía dos contenedores sin cerrar y una tarjeta con la clase `tarifas` en lugar de `tarifa`, por lo que recibía un diseño distinto.
- Los tres enlaces de contratación apuntaban a `#` y no realizaban ninguna acción.
- El CSS tenía una adaptación básica a 900 px, pero la navegación, la tipografía y las tarjetas necesitaban un diseño específico para móvil.
- No existían imágenes, favicon, formularios, filtros, secciones comerciales ni footer.

## Conservado

Nombre Gym Force, combinación negro/blanco/amarillo, lema «Supera tus límites», navegación entre inicio y tarifas y planes mensual, trimestral y anual con los precios originales: 29,99 €, 79,99 € y 249,99 €.

## Implementado

Ocho páginas HTML5 con estructura semántica, navegación y pie compartidos visualmente. Portada con hero, filosofía, instalaciones, clases, equipo, biblioteca, tarifas y contacto. Seis zonas de instalaciones, siete clases filtrables, tres perfiles ficticios y 14 ejercicios con grupos musculares, búsqueda, técnica y cantidades orientativas.

Tarifas comparables por periodo, plan anual destacado, preguntas frecuentes y selección de plan. Contacto demostrativo con contexto de consulta, validación y confirmación explícita sin transmisión. Recursos locales, tipografía con licencia, imágenes WebP, metadata, favicon, enlace de salto, foco visible y respeto al movimiento reducido.

Las pruebas de `tests/smoke.py` verifican los recorridos e interacciones; las capturas y resultados de la entrega se guardan fuera del checkout. No se han añadido dependencias de ejecución ni backend.

## Límite de esta fase

El catálogo público es navegable y demostrativo. No se tramitan altas, pagos o reservas, no hay autenticación y no existen integraciones reales de correo, WhatsApp o mapas. La información del gimnasio está identificada como ficticia. El esquema de evolución queda documentado para una futura aplicación.

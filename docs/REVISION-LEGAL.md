# Revisión legal de la demostración — 23 de octubre de 2026

Estado: entrega para revisión del usuario en la rama `gymforce-vista-previa`, preparada como descarga ZIP. No se modifica `main` ni se despliega esta revisión. La publicación anterior de GitHub Pages permanece intacta.

## Alcance y funcionamiento comprobado

- Se revisaron los ocho HTML, `js/main.js`, los estilos, recursos y archivos del proyecto. No hay backend, formularios externos ni integración de pagos.
- Los únicos formularios están en Inicio y Contacto. Solicitan nombre, correo, interés y mensaje para probar la interfaz. Los controles no tienen `name`, el botón está deshabilitado inicialmente y JavaScript cancela el envío antes de validar y mostrar la confirmación. No se ha cambiado esta lógica.
- El contenido de esos campos permanece temporalmente en el documento abierto. El código no lo transmite ni lo persiste; las funciones de restauración o autocompletado del navegador se distinguen de la aplicación.
- Los parámetros de navegación contienen selecciones de plan, clase o entrenador y llegan al alojamiento como parte de la URL solicitada. No contienen el contenido personal escrito en los campos. Los filtros y las búsquedas de ejercicios operan en memoria en el navegador.
- No se encontraron cookies, localStorage, sessionStorage, IndexedDB, service workers, analítica, publicidad, píxeles, recursos remotos incrustados ni servicios nuevos que requieran consentimiento. Las fuentes, imágenes, CSS y JavaScript están alojados en el proyecto. No se añade banner.
- El único enlace externo de los HTML es la declaración de privacidad de GitHub. No se carga automáticamente. El tratamiento técnico del alojamiento se distingue del funcionamiento del formulario: no se han auditado los registros internos ni los plazos del proveedor.

## Modificaciones

- `legal.html`: cuatro secciones con identificadores `aviso-legal`, `privacidad`, `cookies` y `condiciones`; índice interno, fecha de revisión y textos acordes con el carácter ficticio del proyecto.
- Los ocho HTML: cuatro enlaces diferenciados en el footer. Inicio y Contacto añaden un enlace de privacidad junto al aviso de formulario demostrativo.
- `css/estilos.css`: estilos acotados a los apartados legales, su navegación y los enlaces del footer/formulario. Se conservan la paleta y tipografías existentes.
- `tests/smoke.py`: comprobación de los enlaces del footer, navegación legal móvil, ambos formularios y almacenamiento, ausencia de recursos de terceros y funcionamiento bajo el prefijo `/gymforce/`.
- `README.md` y este documento: estado y alcance de la revisión.
- Sin cambios en `js/main.js`, fotografías, perfiles, precios ni lógica de las demás funciones.

## Validación realizada

Comando:

```sh
python3 tests/smoke.py --artifacts /workspace/gymforce-legal-review --axe /tmp/gymforce-tools/node_modules/axe-core/axe.min.js
```

- 72 combinaciones de página y anchura (ocho páginas; 1440, 1101, 1024, 768, 760, 430, 390, 375 y 320 px): sin desbordamientos detectados; títulos e imágenes correctos.
- 16 revisiones axe en escritorio y móvil: sin infracciones detectadas por las reglas WCAG A/AA y WCAG 2.1 AA utilizadas. No equivale a una auditoría integral de accesibilidad.
- Enlaces locales, recursos, anclas e identificadores sin errores. Los cuatro enlaces legales están presentes en los ocho pies. Las anclas de la página legal funcionan en móvil y no quedan ocultas bajo la cabecera.
- Pruebas de ambos formularios: introducir y validar datos ficticios no genera peticiones de red; no aparecen datos de campos en la URL, cookies, localStorage, sessionStorage, IndexedDB ni registros de service workers en el contexto limpio de prueba.
- No se registraron peticiones de recursos de terceros al recorrer las ocho páginas. Esta prueba local no verifica las cabeceras o prácticas del alojamiento real.
- Menú móvil, filtros, planes, consultas, perfiles, ejercicios y navegación sin JavaScript correctos. Sin excepciones de JavaScript. Sintaxis de JavaScript y `git diff --check` correctos.
- Revisión visual de la página legal en escritorio y móvil mediante capturas.
- El prefijo `/gymforce/` se sirve por HTTP estático local para comprobar las rutas usadas en GitHub Pages. No se han introducido dependencias de servidor, pasos de compilación o rutas absolutas.

Limitaciones: la comprobación remota de `https://alvaroruizdelope-svg.github.io/gymforce/` fue bloqueada por el proxy del entorno (`403 Forbidden` al establecer el túnel). No se afirma que se haya comprobado su disponibilidad o la nueva revisión en producción. No se ha publicado esta revisión. El navegador administrado también bloquea `file://`; ese recorrido se informa como BLOCKED, no como aprobado. No se ha realizado una auditoría jurídica integral ni pruebas en dispositivos físicos o todos los navegadores.

## Si se convierte en un negocio real

Antes de activar funciones comerciales, adaptar la información y la implementación a la actividad efectiva:

- Identificar al titular real y sus datos de contacto, fiscales y registrales que correspondan; verificar la sede, las ofertas, los horarios, las cualificaciones anunciadas y los derechos de uso de fotografías e imagen de las personas.
- Documentar qué datos se recogen, las finalidades y bases jurídicas, responsables/proveedores, destinatarios y transferencias, conservación y ejercicio de derechos; proporcionar un contacto real. Evaluar específicamente datos de salud si se incorporan.
- Implementar y revisar la seguridad del backend, formularios, cuentas y reservas antes de recoger datos reales. No basta con cambiar el texto del formulario.
- Revisar el alojamiento y los contratos con proveedores. Actualizar cookies y mecanismos de consentimiento según las tecnologías efectivas; bloquear previamente las que lo requieran.
- Redactar condiciones de contratación acordes con precios e impuestos, pagos, renovaciones, bajas/cancelaciones, reembolsos y los derechos de las personas consumidoras que resulten aplicables.
- Revisar la información sobre entrenamiento y las obligaciones aplicables con asesoramiento profesional ajustado al negocio.

Estos puntos son cuestiones pendientes de adaptar y verificar, no una declaración de cumplimiento normativo.

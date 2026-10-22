# Evolución hacia una aplicación

La fase actual resuelve la web pública. El siguiente trabajo debe mantenerla utilizable como sitio estático hasta que exista un servidor real. No se debe simular seguridad con JavaScript ni almacenar contraseñas o información personal en localStorage.

## Orden de implementación

1. Diseñar registro, acceso y recuperación junto con un servidor que valide y gestione sesiones seguras. Añadir políticas y tratamientos de datos reales.
2. Incorporar Mi cuenta: perfil, plan, próximas clases y reservas propias. Proteger cada operación en el servidor.
3. Implementar reservas y cancelaciones con disponibilidad y transacciones en base de datos. Evitar duplicados y exceso de aforo incluso con solicitudes simultáneas.
4. Separar administración por permisos, con gestión de usuarios, entrenadores, actividades, planes y reservas, y registro de operaciones relevantes.
5. Incorporar rutinas y mediciones solo cuando su uso, privacidad y requisitos estén definidos.

## Modelo relacional de partida

Propuesta para MySQL/MariaDB; no se han creado tablas ni migraciones en esta fase.

| Tabla         | Datos principales y relaciones                                                |
| ------------- | ----------------------------------------------------------------------------- |
| usuarios      | `id` PK, email normalizado UNIQUE, hash de contraseña, nombre, rol, fechas    |
| planes        | `id` PK, nombre, duración, precio DECIMAL, estado activo                      |
| suscripciones | `id` PK, `usuario_id` FK, `plan_id` FK, fechas y estado                       |
| entrenadores  | `id` PK, nombre, especialidad, presentación, estado activo                    |
| clases        | `id` PK, `entrenador_id` FK, nombre, inicio, duración, aforo positivo         |
| reservas      | `id` PK, `usuario_id` FK, `clase_id` FK, estado y fecha; UNIQUE usuario/clase |
| ejercicios    | `id` PK, grupo muscular, nombre, descripción y técnica                        |
| mediciones    | `id` PK, `usuario_id` FK, fecha y medidas expresamente autorizadas            |

Cada fila de clases representa una sesión reservable concreta; un catálogo o recurrencias pueden separarse si se necesitan. Indexar reservas por clase/estado y usuario/fecha; clases por fecha; suscripciones por usuario/estado; mediciones por usuario/fecha. Usar FK y restricciones de fechas, aforos y cantidades para conservar coherencia. Elegir las políticas de eliminación según la conservación necesaria, evitando cascadas que borren historial por accidente.

Las reservas requieren comprobar el aforo dentro de una transacción, con bloqueos o una operación atómica apropiada. La recuperación de contraseña requiere tokens de un solo uso, caducidad y almacenamiento seguro; el acceso requiere límites de intentos, cookies seguras y defensa CSRF cuando corresponda. Todo ello se valida con pruebas del servidor antes de conectarlo a la interfaz pública.

# Drivers arquitectónicos – EcoRecicla AQP

## 1. Requisitos funcionales clave

| ID | Requisito | Actor | Prioridad |
|---|---|---|---|
| RF-01 | Registrar solicitudes de recojo domiciliario de residuos reciclables (clasificados por tipo: plástico, papel/cartón, vidrio, metal) indicando dirección, coordenadas y franja horaria preferente. | Vecino | Alta |
| RF-02 | Generar y consultar la ruta del día con paradas ordenadas, datos del domicilio y estado de cada solicitud (pendiente, completada, no recolectada). | Reciclador | Alta |
| RF-03 | Registrar in situ la confirmación de recojo junto con el pesaje exacto (en kilogramos) desglosado por tipo de material reciclable recibido. | Reciclador | Alta |
| RF-04 | Acumular, consultar balance histórico y solicitar el canje de puntos ecológicos obtenidos por entrega de material reciclable por beneficios o incentivos municipales. | Vecino | Media |
| RF-05 | Generar reportes consolidados y descargables de toneladas métricas recolectadas, clasificados por distrito, tipo de material, reciclador y rango temporal. | Municipalidad | Alta |
| RF-06 | Gestionar distritos, sectores de cobertura y formalización de asociaciones de recicladores con sus áreas geográficas de atención asignadas. | Municipalidad | Media |

## 2. Atributos de calidad (ordenados por prioridad)

1. **Modificabilidad:** Es el atributo crítico del caso. El sistema debe permitir incorporar un nuevo distrito municipal o configurar una nueva regla de cálculo y canje de puntos con mínimo esfuerzo técnico y sin generar impacto regresivo ni modificaciones en el código de los demás módulos.
2. **Capacidad de interacción (Usabilidad):** Los recicladores laboran en campo, frecuentemente con dispositivos móviles de gama de entrada y bajo luz solar; el registro de paradas y pesaje debe ser sumamente directo y requerir la mínima cantidad de interacciones táctiles.
3. **Eficiencia de desempeño (Rendimiento):** En horarios pico de apertura de turno e inicio de recojo, el sistema debe atender peticiones concurrentes de consulta de rutas y registro de solicitudes manteniendo baja latencia en un servidor con recursos limitados.
4. **Fiabilidad (Disponibilidad y Tolerancia a Fallos):** El sistema debe garantizar que ninguna solicitud de recojo ni registro de pesaje se pierda ante cortes temporales de conectividad móvil en distritos con cobertura 3G inestable.

## 3. Restricciones

| ID | Tipo | Restricción |
|---|---|---|
| R-01 | Plazo | El MVP debe estar completamente implementado, validado y puesto en producción en un plazo estricto de 1 mes (4 semanas). |
| R-02 | Equipo | Equipo compuesto por 3 desarrolladores con experiencia previa en Python y Django, sin especialista exclusivo en infraestructura o DevOps. |
| R-03 | Presupuesto | Presupuesto reducido asignado al proyecto; el despliegue debe realizarse en un único Servidor Privado Virtual (VPS básico: 2 vCPU, 4 GB RAM) evitando servicios cloud administrados de alta tarificación. |
| R-04 | Normativa | Cumplimiento obligatorio de la Ley N.º 29733 (Ley de Protección de Datos Personales del Perú) para datos de vecinos y recicladores, y alineación con los lineamientos del D.L. N.º 1278 (Ley de Gestión Integral de Residuos Sólidos) respecto a la formalización y registro métrico de recicladores. |

## 4. Escenarios de atributos de calidad

| ID | Atributo | Fuente | Estímulo | Entorno | Artefacto | Respuesta | Medida |
|---|---|---|---|---|---|---|---|
| QA-01 | Modificabilidad (Crítico) | Desarrollador de la aplicación | Se requiere incorporar un nuevo distrito de Arequipa o una nueva regla de cálculo de puntos por kilogramo | Entorno de desarrollo y pruebas de integración | Módulo de Puntos o Módulo de Cobertura Distrital | Se añade la nueva regla o distrito mediante un adaptador/estrategia modular sin editar el código fuente de los módulos de Solicitudes, Rutas ni Reportes | Esfuerzo de desarrollo ≤ 2 días-persona; 0 líneas de código modificadas en módulos externos; 100% de la suite de pruebas automatizadas pasa sin regresión |
| QA-02 | Capacidad de interacción (Usabilidad) | Reciclador en ruta | Registra la confirmación de visita y el pesaje (kg) de material entregado por un vecino | Smartphone Android de gama de entrada (2 GB RAM) con conectividad 3G en campo | Interfaz de usuario móvil (PWA) del módulo de Recojo y Rutas | La aplicación valida los datos de pesaje y emite confirmación visual inmediata de registro | Flujo completado en ≤ 4 toques en pantalla; tiempo de renderizado de la confirmación visual ≤ 1.5 s |
| QA-03 | Eficiencia de desempeño (Rendimiento) | 200 usuarios concurrentes (vecinos enviando solicitudes y recicladores consultando sus rutas) | Peticiones HTTP concurrentes a las APIs de consulta de hoja de ruta y creación de solicitud de recojo | Hora pico de la mañana (07:00 a 08:30 a. m.), operación normal sobre el VPS de producción | API REST de la aplicación (Módulos de Solicitudes y Rutas) | La API procesa las solicitudes, consulta la base de datos y entrega las respuestas JSON formateadas | Percentil 95 del tiempo de respuesta (p95) ≤ 2.0 s; tasa de respuestas con error HTTP 5xx ≤ 0.1% |

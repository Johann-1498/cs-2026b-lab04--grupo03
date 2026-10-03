# ADR-002: Estrategia de persistencia con PostgreSQL y esquemas modulares

- Estado: Aceptado
- Fecha: 2026-10-01
- Decisores: Equipo de desarrollo (3 devs)

## Contexto

El sistema requiere persistir solicitudes de recojo, rutas, pesajes, balances de puntos y reportes municipales sobre un único VPS (**R-03**), manteniendo el aislamiento lógico entre los módulos del monolito modular para garantizar la modificabilidad (**QA-01**) y cumplir con los requisitos de trazabilidad de residuos (**RF-03**, **RF-05**).

## Alternativas consideradas

1. Base de datos única con tablas altamente acopladas mediante claves foráneas cruzadas entre todas las apps.
2. Múltiples bases de datos físicas independientes (una por módulo), descartada por exceder los límites de gestión de conexiones y recursos en un VPS único.
3. Base de datos PostgreSQL compartida pero con separación lógica de esquemas o tablas estrictamente delimitadas por aplicación del monolito modular: elegida.

## Decisión

Usaremos una única instancia de PostgreSQL en el VPS, utilizando el ORM de Django con migraciones separadas por cada app modular (`solicitudes`, `rutas`, `puntos`, `reportes`, `distritos`). Se prohíben estrictamente las consultas directas entre tablas de diferentes módulos a nivel de ORM, forzando que cada módulo acceda únicamente a su propio conjunto de tablas.

## Consecuencias

- Positivas: simplicidad en la administración y respaldos (un solo dump de PostgreSQL), transacciones atómicas eficientes y cero overhead de red de bases de datos distribuidas.
- Negativas / riesgos: se debe tener cuidado en las migraciones para evitar dependencias circulares de claves foráneas entre dominios.

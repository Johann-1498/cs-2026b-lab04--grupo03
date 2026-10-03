# ADR-001: Adoptar un monolito modular para el MVP de EcoRecicla AQP

- Estado: Aceptado
- Fecha: 2026-10-01
- Decisores: Equipo de desarrollo (3 devs) y Product Owner

## Contexto

El sistema debe estar en producción en un plazo estricto de 1 mes (**R-01**), operado por un equipo de 3 desarrolladores Python/Django sin especialista DevOps (**R-02**), desplegado en un único VPS modesto (**R-03**). Asimismo, el driver más crítico es la modificabilidad (**QA-01**), que exige incorporar nuevos distritos o reglas de cálculo de puntos en $\le 2$ días-persona sin alterar otros módulos.

## Alternativas consideradas

1. Monolito en Capas Tradicional (puntaje 3.90): desarrollo inicial rápido, pero acoplamiento elevado que viola la modificabilidad (QA-01).
2. Microservicios orientados a eventos (puntaje 2.50): alta escalabilidad, pero inviable por consumo de recursos en VPS único y complejidad operativa inalcanzable para 3 devs en 1 mes.
3. Monolito Modular con Puertos y Adaptadores (puntaje 4.45): elegido.

## Decisión

Usaremos un monolito modular en Django organizado en 5 dominios (`solicitudes`, `rutas`, `puntos`, `reportes`, `distritos`). Los módulos se comunicarán exclusivamente a través de interfaces públicas explícitas (`services.py`). Las reglas variables de cálculo de puntos e integración distrital se implementarán mediante el patrón *Strategy* / adaptadores.

## Consecuencias

- Positivas: un único despliegue económico en el VPS, desarrollo ágil en 1 mes, alta modificabilidad para nuevos distritos y reglas sin efectos colaterales.
- Negativas / riesgos: se requiere disciplina estricta de equipo y validación automática en CI (con `import-linter`) para evitar la erosión de los límites modulares.

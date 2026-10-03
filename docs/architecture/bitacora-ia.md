# Bitácora de uso de IA – EcoRecicla AQP

| # | Fecha | Herramienta | Prompt (resumen) | Qué propuso la IA | Qué verificamos o corregimos | Decisión |
|---|---|---|---|---|---|---|
| 1 | 01/10/2026 | Antigravity CLI | Genera drivers.md para EcoRecicla AQP siguiendo la plantilla de la guía: requisitos, atributos de calidad, restricciones y 3 escenarios de 6 partes con medidas numéricas. | 6 RF (RF-01 a RF-06), 4 atributos priorizados (Modificabilidad como crítico), 4 restricciones (R-01 a R-04) y 3 escenarios QA-01 a QA-03 con medidas numéricas. | Se verificó que todas las medidas fueran numéricas y verificables (sin términos vagos), que R-01 (MVP en 1 mes) y R-02 (equipo de 3 devs en Python/Django) estuvieran presentes, y que el atributo crítico QA-01 cumpliera la medida de ≤ 2 días-persona y 0 módulos externos afectados. | Aceptada (con ajustes menores de redacción) |
| 2 | 01/10/2026 | Antigravity CLI | Propón 3 alternativas de estilo arquitectónico para EcoRecicla AQP con estas restricciones: MVP en 1 mes, 3 devs Python/Django, VPS único, atributo crítico = modificabilidad (≤ 2 días-persona). Tabla comparativa + recomendación. | A) Monolito en Capas, B) Monolito Modular con Puertos y Adaptadores, C) Microservicios orientados a eventos. | Se verificó que cada alternativa respetara R-01 (1 mes) y R-02 (3 devs), y que no se inventaran servicios de pago ni APIs inexistentes. | Aceptada (las 3 alternativas son viables de analizar) |
| 3 | 01/10/2026 | Antigravity CLI | Actúa como abogado del diablo y critica la alternativa que recomendaste. Enumera 5 riesgos graves y para cada uno una táctica de mitigación. | Riesgos sobre acoplamiento, costos ocultos de microservicios y sobrecarga operativa. | Se verificó que las críticas apuntaran a nuestras restricciones reales (R-01, R-02, R-03) y no a supuestos genéricos. | Aceptada (se usó para justificar la matriz) |

> Pegue los prompts completos debajo de la tabla (sección "Anexo: Prompts completos").  
> Nunca incluya datos personales ni información confidencial en un prompt.

## Anexo: Prompts completos

### Prompt 1: Generación de drivers arquitectónicos
```text
Genera el contenido completo de docs/architecture/drivers.md siguiendo la plantilla de la sección "Paso 9" de la guía.
Incluye: mínimo 5 requisitos funcionales con actor y prioridad, mínimo 4 atributos de calidad priorizados, mínimo 4 restricciones (R-01 = MVP en 1 mes obligatoria, R-02 = equipo 3 devs Python/Django), y 3 escenarios de calidad de 6 partes (uno debe ser modificabilidad).
Todas las medidas deben ser numéricas.
No inventes APIs ni normativas; si no estás seguro, dilo.
Escribe directamente el archivo drivers.md.
```

### Prompt 2: Generación de alternativas arquitectónicas
```text
Ahora actúa como arquitecto de software senior con experiencia en sistemas para municipalidades y PYMES.
Contexto: D:\UNSA\Cursos\2026-B\CS\LAB\Lab04\docs\architecture\drivers.md
Restricciones: <las mismas>
Tarea: propón 3 alternativas de estilo arquitectónico para EcoRecicla.
Para cada una: fortalezas, debilidades, riesgos y qué atributos de calidad favorece o penaliza.
Formato: tabla comparativa Markdown + recomendación justificada.
No inventes APIs; si no estás seguro, indícalo.
```

### Prompt 3: Crítica adversarial ("Abogado del diablo")
```text
Actúa como "abogado del diablo". Critica duramente la alternativa que recomendaste: ¿qué supuestos no se cumplen con nuestras restricciones? ¿Qué podría fallar en producción? ¿Qué costo oculto tiene? Enumera 5 riesgos graves y para cada uno una táctica de mitigación.
```

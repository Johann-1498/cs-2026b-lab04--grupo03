# Matriz de decisión – EcoRecicla AQP

## Alternativas

- **A. Monolito en Capas Tradicional (Django MVT):** El sistema se organiza horizontalmente en capas de presentación, lógica de negocio y datos sobre un único proyecto Django. Todos los módulos comparten directamente modelos del ORM y un esquema unificado de base de datos relacional.
- **B. Monolito Modular con Puertos y Adaptadores:** El sistema se mantiene en un único despliegue ejecutable, pero organizado internamente en módulos de dominio autónomos (`solicitudes`, `rutas`, `puntos`, `reportes`, `distritos`). Cada módulo expone contratos públicos explícitos (`services.py`), oculta su persistencia y usa adaptadores para reglas dinámicas de puntos y distritos.
- **C. Microservicios Orientados a Eventos:** Descomposición del sistema en servicios autónomos e independientes físicamente, cada uno con base de datos propia (*database-per-service*), comunicados a través de un API Gateway y un broker de mensajes asíncronos (RabbitMQ/Redis).

## Criterios y pesos (deben sumar 100 %)

| Criterio | Peso | Justificación (driver relacionado) |
|---|:---:|---|
| **Modificabilidad** | 30 % | **QA-01 (Atributo Crítico):** Incorporar un nuevo distrito o regla de cálculo de puntos en ≤ 2 días-persona sin alterar otros módulos. |
| **Tiempo de entrega** | 25 % | **R-01:** Plazo estricto de 1 mes (4 semanas) para tener el MVP completo y validado en producción. |
| **Simplicidad operativa y experiencia de equipo** | 20 % | **R-02:** Equipo de 3 desarrolladores con experiencia en Python/Django, sin especialista dedicado en DevOps ni administración de infraestructura compleja. |
| **Viabilidad económica y de hosting** | 15 % | **R-03:** Presupuesto bajo que restringe el despliegue a un único Servidor Privado Virtual (VPS modesto: 2 vCPU, 4 GB RAM). |
| **Eficiencia de desempeño y estabilidad** | 10 % | **QA-03:** Tiempos de respuesta p95 ≤ 2.0 s y tasa de error ≤ 0.1% durante picos de concurrencia matutina de recojo. |

## Matriz (puntaje 1 = muy malo ... 5 = excelente)

| Criterio (peso) | A: Monolito en Capas | B: Monolito Modular | C: Microservicios |
|---|:---:|:---:|:---:|
| Modificabilidad (30 %) | 2 | 5 | 5 |
| Tiempo de entrega (25 %) | 5 | 4 | 1 |
| Simplicidad operativa (20 %) | 5 | 4 | 1 |
| Viabilidad económica / VPS (15 %) | 5 | 5 | 1 |
| Eficiencia de desempeño (10 %) | 3 | 4 | 4 |
| **Total ponderado** | **3.90** | **4.45** | **2.50** |

*Cálculo del total ponderado:*
- **Alternativa A:** $(0.30 \times 2) + (0.25 \times 5) + (0.20 \times 5) + (0.15 \times 5) + (0.10 \times 3) = 0.60 + 1.25 + 1.00 + 0.75 + 0.30 = \mathbf{3.90}$
- **Alternativa B:** $(0.30 \times 5) + (0.25 \times 4) + (0.20 \times 4) + (0.15 \times 5) + (0.10 \times 4) = 1.50 + 1.00 + 0.80 + 0.75 + 0.40 = \mathbf{4.45}$
- **Alternativa C:** $(0.30 \times 5) + (0.25 \times 1) + (0.20 \times 1) + (0.15 \times 1) + (0.10 \times 4) = 1.50 + 0.25 + 0.20 + 0.15 + 0.40 = \mathbf{2.50}$

## Conclusión

Elegimos la **Alternativa B: Monolito Modular con Puertos y Adaptadores (puntaje 4.45)**. 

Esta arquitectura satisface plenamente el atributo crítico de modificabilidad (**QA-01**) al encapsular las reglas de puntos y distritos mediante interfaces desacopladas, permitiendo extensiones en $\le 2$ días-persona sin provocar cambios regresivos en el resto del sistema. A la vez, se mantiene dentro de los límites estrictos de viabilidad del proyecto: un único despliegue operado por 3 desarrolladores Django (**R-02**) sobre un único VPS económico (**R-03**) para salir a producción en 1 mes (**R-01**).

La Alternativa A (3.90), aunque rápida de implementar inicialmente, fue descartada como opción principal debido a su alto riesgo de acoplamiento que compromete la modificabilidad futura (será documentada en el diagrama PlantUML de alternativa descartada). La Alternativa C (2.50) fue descartada categóricamente por su inalcanzable sobrecarga operativa y de consumo de recursos en el VPS.

Para mayor detalle de la decisión formal, consultar el [ADR-001: Estilo arquitectónico](adr/001-estilo-arquitectonico.md).

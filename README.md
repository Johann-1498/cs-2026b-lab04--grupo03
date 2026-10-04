# EcoRecicla AQP – Laboratorio 04: Fundamentos de arquitectura de software
Construcción de Software - EPIS-UNSA - 2026-B - Grupo 03

## Integrantes

| Nombre | Rol en el laboratorio |
|---|---|
| Caceres Ruiz, Johann Andre | Redactor de Drivers y ADRs |
| Velarde Saldaña, Jhossep Fabritzio | Diagramador (Mermaid, PlantUML, Python Diagrams) |
| Coaquira Suyo, Gabriela Dayana | Verificador de IA y Bitácora |

## Caso

EcoRecicla AQP es una plataforma tecnológica para gestionar el recojo de residuos reciclables domiciliarios en coordinación con recicladores formalizados en distritos de Arequipa. Conecta a vecinos, recicladores en ruta y administradores municipales mediante solicitudes, generación de rutas de recojo, puntos canjeables y reportes de toneladas recicladas. El **atributo de calidad crítico** es la **modificabilidad**, exigiendo incorporar nuevos distritos o reglas de cálculo de puntos en $\le 2$ días-persona sin alterar los demás módulos.

## Arquitectura elegida (Monolito Modular)

```mermaid
flowchart TB
    VEC["Vecino"]
    REC["Reciclador"]
    MUN["Administrador Municipal"]
    subgraph APP["EcoRecicla AQP – Monolito modular (Django)"]
        API["Capa de presentación: API REST + PWA"]
        M1["Solicitudes y Registro"]
        M2["Gestión de Rutas"]
        M3["Puntos y Canjes"]
        M4["Reportes y Métricas"]
        M5["Distritos y Cobertura"]
    end
    INF["Capa de infraestructura: ORM y adaptadores"]
    DB[("PostgreSQL\n(Esquemas modulares)")]
    EXT["Servicios externos\n(Notificaciones / Incentivos)"]
    VEC & REC & MUN --> API
    API --> M1 & M2 & M3 & M4 & M5
    M1 & M2 & M3 & M4 & M5 --> INF
    INF --> DB
    INF --> EXT
    classDef mod fill:#E8F5E9,stroke:#2E7D32,color:#000
    classDef ext fill:#F2F2F2,stroke:#7F7F7F,color:#000,stroke-dasharray: 4 3
    classDef usr fill:#FDEDEC,stroke:#C8310E,color:#000
    class M1,M2,M3,M4,M5 mod
    class EXT ext
    class VEC,REC,MUN usr
```

## Decisiones arquitectónicas (ADR)

- [ADR-001: Estilo arquitectónico (Monolito Modular)](docs/architecture/adr/001-estilo-arquitectonico.md)
- [ADR-002: Estrategia de base de datos PostgreSQL](docs/architecture/adr/002-base-de-datos.md)
- [ADR-003: Autenticación con JWT](docs/architecture/adr/003-autenticacion.md)

## Reflexión sobre el uso de la IA (5-8 líneas)

La asistencia de IA fue de gran utilidad para estructurar rápidamente los escenarios de calidad de 6 partes, redactar borradores de ADR y proponer alternativas arquitectónicas iniciales. Sin embargo, se identificó que la IA tendía a sesgarse hacia microservicios hipercomplejos por "moda", ignorando las restricciones reales de 1 mes de plazo y 3 desarrolladores. Esto demostró la vigencia de la regla de oro: la IA propone, pero el equipo verifica críticamente, ajusta y valida cada decisión contra los drivers técnicos y presupuestarios del proyecto.

# ADR-003: Mecanismo de autenticación y control de accesos

- Estado: Aceptado
- Fecha: 2026-10-01
- Decisores: Equipo de desarrollo (3 devs)

## Contexto

El sistema atiende a tres tipos de actores con privilegios diferenciados: Vecinos, Recicladores y Administradores Municipales. Debe garantizarse el cumplimiento de la Ley N.º 29733 de Protección de Datos Personales (**R-04**), además de ofrecer autenticación ágil para recicladores en campo mediante dispositivos móviles de gama baja (**QA-02**).

## Alternativas consideradas

1. Autenticación basada en sesiones tradicionales de Django (Cookies HTTPOnly): segura, pero compleja para PWA en dispositivos móviles con conectividad intermitente.
2. Tokens JWT (*JSON Web Tokens*) sin estado (stateless) con expiración corta y almacenamiento seguro en LocalStorage/SessionStorage de la PWA: elegida.
3. OAuth2 / OpenID Connect completo con proveedor externo (Keycloak / Auth0), descartado por complejidad de despliegue y sobrecarga de infraestructura en el VPS (**R-03**).

## Decisión

Implementaremos autenticación basada en JWT utilizando *djangorestframework-simplejwt*. Los tokens de acceso tendrán una duración corta (1 hora) y los de refresco (refresh tokens) durarán 7 días, permitiendo que los recicladores mantengan su sesión activa durante su jornada laboral en campo sin reautenticarse constantemente.

## Consecuencias

- Positivas: interoperabilidad limpia entre la API REST y la PWA del reciclador, fácil gestión de roles (Vecino, Reciclador, Admin) mediante claims y bajo consumo de recursos en el VPS.
- Negativas / riesgos: necesidad de gestionar adecuadamente la revocación de tokens y el almacenamiento cifrado en el cliente móvil.

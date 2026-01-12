# Anti-Bot Security System with Risk Scoring

Sistema de seguridad diseñado para **detectar, clasificar y mitigar bots maliciosos** en aplicaciones web mediante **análisis de comportamiento, rate limiting y un motor de Risk Scoring**, siguiendo principios utilizados en entornos **SOC** y **WAFs modernos**.

---

## Objetivo del proyecto

El objetivo de este proyecto es simular cómo funcionan los sistemas reales de detección de amenazas en tráfico web, permitiendo:

- Identificar tráfico automatizado (bots)
- Evaluar el nivel de riesgo de cada solicitud
- Aplicar decisiones automáticas (permitir o bloquear)
- Generar eventos de seguridad listos para integración con un SIEM

Este proyecto fue desarrollado con fines **educativos y profesionales**, enfocado en ciberseguridad defensiva (Blue Team) y validación ofensiva (Red Team).

---

## Enfoque de seguridad

El sistema implementa conceptos reales de la industria:

- **Risk Scoring** (puntuación de riesgo)
- **Rule-Based Detection**
- **Behavioral Analysis**
- **Logging tipo SIEM**
- **Respuesta automática a incidentes**

---

## Arquitectura general

```text
Cliente
  ↓
Anti-Bot Middleware
  ├─ Fingerprinting
  ├─ Rate Limiting
  ├─ Risk Scoring
  ├─ Logging de eventos
  ↓
Decisión (ALLOW / BLOCK)
  ↓
Aplicación protegida


# OPTIMIZACIÓN DE ADS & ROI: PROYECTO CYGNUS STYLE 🚀

> **Python · Power BI · Grafana · Meta Ads · Google Ads · TikTok · LinkedIn**

---

## 📊 Resultados clave

| Métrica | Valor |
|---|---|
| 💰 ROI global | **253%** — por cada $1 invertido, retorna $3,53 |
| 📈 Revenue generado | **$4.170.000** en 20 campañas |
| 💸 Gasto total | **$1.179.800** (98.2% ejecutado) |
| 🔴 Campañas con pérdida | **2 identificadas** y pausadas |
| ⏱️ Horas ahorradas | **12hs/mes** de reportes manuales |

---

## 📉 Rendimiento por plataforma

```
Google   ROI 251.6%  ████████████████████████████░░  ✅ Excelente
Meta     ROI 233.5%  ███████████████████████████░░░  ✅ Excelente
TikTok   ROI 131.4%  █████████████████░░░░░░░░░░░░░  ⚠️  Revisar
LinkedIn ROI  66.4%  █████████░░░░░░░░░░░░░░░░░░░░░  ⚠️  Revisar
DSP      ROI -31.1%  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  🔴 Pausar
```

---

## 🔽 Embudo de conversión (funnel)

```
Impresiones  ████████████████████████████████████████  18.600.000
             ↓ se caen el 93,3% → problema creativo
Clics        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     114.200  (CTR 0,6%)
             ↓ se caen el 98,0% → problema de landing
Conversiones █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░       2.243  (Conv 2,0%)
```

> El mayor drop ocurre entre impresiones y clics → oportunidad de mejora en creatividades y segmentación.

---

## ⚡ Sistema de alertas — Grafana

```
[08:03] 🔴 ALERTA: Display Branding → ROI -39.6% — acción requerida
[08:01] 🟢 OK: Google Shopping → ROI 478% — rendimiento óptimo
[08:00] 🟢 Pipeline completado — 20 campañas procesadas
```

Tiempo de respuesta ante ROI negativo: **< 5 minutos** (automático)

---

## EL PROBLEMA (CONTEXTO)

Un cliente presentaba una **alta dispersión en sus costos de adquisición** y no lograba identificar qué campañas estaban generando pérdida de inversión debido a la falta de monitoreo en tiempo real.

## ¿CÓMO LO RESOLVÍ?

* **AUTOMATIZACIÓN**: Diseñé un script en **Python** que consolida y limpia los datos de 20 campañas, logrando un ahorro de **12 horas mensuales** en la generación de reportes manuales.
* **ANÁLISIS CRÍTICO**: Identifiqué 2 campañas con **ROI negativo**, permitiendo la redirección del presupuesto y alcanzando un rendimiento global del **253%**.
* **DIFERENCIADOR**: Implementé alertas automáticas en **Grafana** que notifican en menos de **5 minutos** si el rendimiento cae por debajo del umbral aceptable.

## STACK TECNOLÓGICO

* **PYTHON (PANDAS)**: Procesamiento de embudos de conversión y cálculo de métricas clave (CTR, CPL, CPC).
* **POWER BI**: Dashboard interactivo con filtros dinámicos por campaña y visualización del funnel.
* **GRAFANA**: Monitoreo de performance en tiempo real y alertas proactivas.

## ESTRUCTURA DEL REPO (FILES)

* `roi_funnel_analysis.py`: El script principal de limpieza y cálculo de ROI.
* `campanas_sucio.csv`: El set de datos crudos con inconsistencias de plataforma.
* `grafana_setup.json`: Configuración técnica para el sistema de alertas de monitoreo.
* `dashboard_guia.py`: Lógica DAX y estructura para la réplica del tablero en Power BI.
* `reporte_final.html`: El entregable visual consolidado para la toma de decisiones.

---

*Este proyecto refleja mi capacidad para unir el análisis de datos técnico con los objetivos de crecimiento del negocio (Growth Marketing).*

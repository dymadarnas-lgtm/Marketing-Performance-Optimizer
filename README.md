# OPTIMIZACIÓN DE ADS & ROI: PROYECTO CYGNUS STYLE 

![Dashboard de Performance](https://github.com/dymadarnas-lgtm/Marketing-Performance-Optimizer/blob/main/dashboard_final.png?raw=true)

Este proyecto demuestra cómo transformar datos caóticos de múltiples plataformas publicitarias (Meta, Google, TikTok, LinkedIn) en decisiones estratégicas de inversión y ahorro de presupuesto.

## EL PROBLEMA (CONTEXTO)
En el sector de marketing digital, la dispersión de datos entre plataformas impide una visión clara del retorno. Un cliente presentaba una **alta dispersión en sus costos de adquisición** y no lograba identificar qué campañas generaban pérdida por la falta de monitoreo en tiempo real.

## ¿CÓMO LO RESOLVÍ?
* **AUTOMATIZACIÓN**: Diseñé un script en **Python** que consolida y limpia los datos de 20 campañas, logrando un ahorro de **12 horas mensuales** en reportes manuales.
* **ANÁLISIS CRÍTICO**: Identifiqué 2 campañas con **ROI negativo**, permitiendo pausar gastos ineficientes de inmediato y mejorar el rendimiento global al **253%**.
* **DIFERENCIADOR**: Implementé alertas automáticas en **Grafana** que notifican en menos de **5 minutos** si el rendimiento cae por debajo del umbral aceptable.

## STACK TECNOLÓGICO
* **PYTHON (PANDAS)**: Procesamiento de embudos de conversión y cálculo de métricas (CTR, CPL, CPC).
* **POWER BI**: Dashboard interactivo con filtros por campaña y visualización del funnel.
* **GRAFANA**: Monitoreo de performance en tiempo real y alertas proactivas.

## ESTRUCTURA DEL REPO
* `roi_funnel_analysis.py`: Script Python que limpia datos y calcula métricas de ROI.
* `campanas_sucio.csv`: Set de datos con errores simulados para demostrar el proceso de limpieza.
* `grafana_setup.json`: Configuración para replicar el sistema de alertas automáticas.
* `reporte_final.html`: Resumen ejecutivo visual con las conclusiones clave del proyecto.

---
*Este proyecto fue parte de mi experiencia técnica optimizando inversiones en el sector de Growth Marketing.*

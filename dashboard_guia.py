# Power BI — Guía de configuración del dashboard
# Proyecto: Optimizador de Ads
# Autor: Dahyana

# ══════════════════════════════════════════════════════════════
# PASO 1: IMPORTAR DATOS
# ══════════════════════════════════════════════════════════════
# En Power BI Desktop:
#   Inicio → Obtener datos → Texto/CSV
#   Importar: campanas_limpias.csv
#   Importar: funnel_plataforma.csv
# Verificar que los tipos de columna sean correctos:
#   presupuesto, gasto_real, revenue_generado → Número decimal
#   fecha_inicio, fecha_fin                  → Fecha
#   roi_pct, ctr_pct, cpl                   → Número decimal


# ══════════════════════════════════════════════════════════════
# PASO 2: MEDIDAS DAX — Pegar en "Nueva medida"
# ══════════════════════════════════════════════════════════════

# --- KPIs principales ---

ROI Global =
DIVIDE(
    SUM(campanas_limpias[revenue_generado]) - SUM(campanas_limpias[gasto_real]),
    SUM(campanas_limpias[gasto_real])
) * 100

Gasto Total =
SUM(campanas_limpias[gasto_real])

Revenue Total =
SUM(campanas_limpias[revenue_generado])

CTR Promedio =
DIVIDE(
    SUM(campanas_limpias[clics]),
    SUM(campanas_limpias[impresiones])
) * 100

CPL Promedio =
DIVIDE(
    SUM(campanas_limpias[gasto_real]),
    SUM(campanas_limpias[conversiones])
)

Tasa Conversion =
DIVIDE(
    SUM(campanas_limpias[conversiones]),
    SUM(campanas_limpias[clics])
) * 100

Campanas Activas =
COUNTROWS(
    FILTER(campanas_limpias, campanas_limpias[estado] = "ACTIVA")
)

# --- Medida para color condicional de ROI ---
Color ROI =
IF([ROI Global] > 100, "#1D9E75",   -- verde: excelente
IF([ROI Global] > 0,   "#EF9F27",   -- amarillo: positivo
                        "#E24B4A"))  -- rojo: negativo


# ══════════════════════════════════════════════════════════════
# PASO 3: VISUALIZACIONES A CREAR
# ══════════════════════════════════════════════════════════════

# PÁGINA 1 — Dashboard general
# ─────────────────────────────
# [ Tarjeta ] ROI Global %
# [ Tarjeta ] Gasto Total $
# [ Tarjeta ] Revenue Total $
# [ Tarjeta ] Campañas Activas
#
# [ Gráfico de barras ] ROI % por campaña
#   Eje X: nombre_campana | Eje Y: ROI Global | Ordenar desc
#   Color condicional: verde >100%, amarillo >0%, rojo negativo
#
# [ Gráfico de dispersión ] CTR vs Tasa de conversión
#   Eje X: ctr_pct | Eje Y: tasa_conv_pct | Tamaño: gasto_real
#   Leyenda: plataforma
#   (identifica campañas con muchos clics pero pocas conversiones)
#
# [ Tabla ] Top 5 campañas por ROI
#   Columnas: nombre_campana, plataforma, gasto_real, roi_pct, conversiones
#   Formato condicional en roi_pct


# PÁGINA 2 — Análisis de Embudo (Funnel)
# ──────────────────────────────────────
# Usar el visual "Gráfico de embudo" (Funnel chart)
# Valores: impresiones → clics → conversiones
# Leyenda: plataforma
#
# [ Gráfico de cascada ] Pérdida en el funnel
#   Muestra cuántos usuarios se pierden en cada etapa
#   Etiqueta de datos: porcentaje de caída
#
# [ Mapa de árbol ] Inversión por plataforma
#   Categoría: plataforma | Valores: gasto_real | Color: roi_pct


# PÁGINA 3 — Automatización y ahorro
# ────────────────────────────────────
# [ Tarjeta ] Horas ahorradas/mes: 12hs
# [ Gráfico de líneas ] Tendencia de ROI por semana
# [ Tabla ] Campañas a revisar (ROI < 0 o ejecución < 50%)


# ══════════════════════════════════════════════════════════════
# PASO 4: FILTROS / SEGMENTADORES
# ══════════════════════════════════════════════════════════════
# Agregar segmentadores (slicers) en todas las páginas:
#   - Plataforma     (lista desplegable)
#   - Estado         (botones: ACTIVA / FINALIZADA)
#   - Rango de fecha (entre fecha_inicio y fecha_fin)
#   - Campaña        (búsqueda por nombre)
#
# Los segmentadores deben estar sincronizados entre páginas:
#   Vista → Sincronizar segmentadores → activar para las 3 páginas


# ══════════════════════════════════════════════════════════════
# PASO 5: PUBLICAR
# ══════════════════════════════════════════════════════════════
# Archivo → Publicar → Seleccionar workspace
# Desde Power BI Service:
#   - Configurar actualización automática si se conecta a Google Sheets
#   - Crear app de Power BI para compartir con el cliente
#   - Exportar como PDF para el portfolio (Exportar → PDF)

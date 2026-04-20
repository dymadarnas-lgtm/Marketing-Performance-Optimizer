"""
Optimizador de Ads — Análisis de ROI y Embudo de Conversión
Autor: Dahyana
Descripción: Limpieza de datos de campañas, cálculo de métricas clave
             (ROI, CPC, CPL, CTR) y análisis de funnel por plataforma.
             Genera archivos listos para Power BI y Grafana.
"""

import pandas as pd
import json
from datetime import datetime

print("=" * 60)
print("  OPTIMIZADOR DE ADS — Análisis de ROI y Funnel")
print("  Dahyana · Portfolio Data Analyst")
print("=" * 60)


# ─────────────────────────────────────────────────────────
# 1. CARGA Y LIMPIEZA DE DATOS
# ─────────────────────────────────────────────────────────
print("\n── Paso 1: Carga y limpieza ─────────────────────────")

df = pd.read_csv("../data/campanas_sucio.csv")
total = len(df)
print(f"✔ {total} campañas cargadas.")

# Normalizar texto
df["nombre_campana"] = df["nombre_campana"].str.strip()
df["plataforma"]     = df["plataforma"].str.strip().str.upper()
df["estado"]         = df["estado"].str.strip().str.upper()

# Rellenar plataformas faltantes
sin_plataforma = df["plataforma"].isna() | (df["plataforma"] == "")
df.loc[sin_plataforma, "plataforma"] = "DESCONOCIDA"
print(f"  ⚠ {sin_plataforma.sum()} campaña(s) sin plataforma → marcadas como DESCONOCIDA")

# Normalizar fechas
def parsear_fecha(f):
    for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]:
        try:
            return datetime.strptime(str(f).strip(), fmt)
        except:
            continue
    return None

df["fecha_inicio"] = df["fecha_inicio"].apply(parsear_fecha)
df["fecha_fin"]    = df["fecha_fin"].apply(parsear_fecha)
sin_inicio = df["fecha_inicio"].isna().sum()
sin_fin    = df["fecha_fin"].isna().sum()
if sin_inicio: print(f"  ⚠ {sin_inicio} campaña(s) sin fecha de inicio.")
if sin_fin:    print(f"  ⚠ {sin_fin} campaña(s) sin fecha de fin (pueden estar activas).")


# ─────────────────────────────────────────────────────────
# 2. CÁLCULO DE MÉTRICAS DE PERFORMANCE
# ─────────────────────────────────────────────────────────
print("\n── Paso 2: Cálculo de métricas ──────────────────────")

# CTR = clics / impresiones * 100
df["ctr_pct"] = (df["clics"] / df["impresiones"] * 100).round(2)

# CPC = gasto / clics (costo por clic)
df["cpc"] = (df["gasto_real"] / df["clics"]).round(2)

# CPL = gasto / conversiones (costo por lead/conversión)
df["cpl"] = (df["gasto_real"] / df["conversiones"]).round(2)

# ROI = (revenue - gasto) / gasto * 100
df["roi_pct"] = ((df["revenue_generado"] - df["gasto_real"]) / df["gasto_real"] * 100).round(1)

# Tasa de conversión = conversiones / clics * 100
df["tasa_conv_pct"] = (df["conversiones"] / df["clics"] * 100).round(2)

# Presupuesto ejecutado %
df["ejecucion_pct"] = (df["gasto_real"] / df["presupuesto"] * 100).round(1)

print("  ✔ CTR, CPC, CPL, ROI, tasa de conversión calculados.")


# ─────────────────────────────────────────────────────────
# 3. ANÁLISIS DE FUNNEL POR PLATAFORMA
# ─────────────────────────────────────────────────────────
print("\n── Paso 3: Análisis de embudo (funnel) ──────────────")

funnel = df.groupby("plataforma").agg(
    impresiones   = ("impresiones",    "sum"),
    clics         = ("clics",          "sum"),
    conversiones  = ("conversiones",   "sum"),
    gasto         = ("gasto_real",     "sum"),
    revenue       = ("revenue_generado","sum"),
    campanas      = ("campana_id",     "count")
).reset_index()

funnel["ctr_pct"]       = (funnel["clics"]       / funnel["impresiones"]  * 100).round(2)
funnel["tasa_conv_pct"] = (funnel["conversiones"] / funnel["clics"]        * 100).round(2)
funnel["roi_pct"]       = ((funnel["revenue"]     - funnel["gasto"])       / funnel["gasto"] * 100).round(1)
funnel["cpl"]           = (funnel["gasto"]        / funnel["conversiones"]).round(2)
funnel = funnel.sort_values("roi_pct", ascending=False)

print("\n  Rendimiento por plataforma:")
print(f"  {'Plataforma':<15} {'Campañas':>8} {'CTR%':>7} {'Conv%':>7} {'ROI%':>8} {'CPL':>8}")
print("  " + "-" * 55)
for _, r in funnel.iterrows():
    print(f"  {r['plataforma']:<15} {int(r['campanas']):>8} {r['ctr_pct']:>7.2f} {r['tasa_conv_pct']:>7.2f} {r['roi_pct']:>8.1f} {r['cpl']:>8.0f}")


# ─────────────────────────────────────────────────────────
# 4. DETECCIÓN DE CAMPAÑAS PROBLEMÁTICAS
# ─────────────────────────────────────────────────────────
print("\n── Paso 4: Campañas con problemas ───────────────────")

# ROI negativo
roi_negativo = df[df["roi_pct"] < 0]
if len(roi_negativo):
    print(f"  ⚠ {len(roi_negativo)} campaña(s) con ROI negativo:")
    for _, r in roi_negativo.iterrows():
        print(f"    → {r['nombre_campana']} | ROI: {r['roi_pct']}%")

# Presupuesto subejecuado (<50% del mes)
df_activas = df[df["estado"] == "ACTIVA"].copy()
sub_exec = df_activas[df_activas["ejecucion_pct"] < 50]
if len(sub_exec):
    print(f"  ⚠ {len(sub_exec)} campaña(s) activa(s) con <50% de presupuesto ejecutado:")
    for _, r in sub_exec.iterrows():
        print(f"    → {r['nombre_campana']} | Ejecutado: {r['ejecucion_pct']}%")

# CTR muy bajo (<0.1%)
ctr_bajo = df[df["ctr_pct"] < 0.1]
if len(ctr_bajo):
    print(f"  ⚠ {len(ctr_bajo)} campaña(s) con CTR menor al 0.1%:")
    for _, r in ctr_bajo.iterrows():
        print(f"    → {r['nombre_campana']} | CTR: {r['ctr_pct']}%")


# ─────────────────────────────────────────────────────────
# 5. RESUMEN EJECUTIVO
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  RESUMEN EJECUTIVO")
print("=" * 60)

gasto_total   = df["gasto_real"].sum()
revenue_total = df["revenue_generado"].sum()
roi_global    = ((revenue_total - gasto_total) / gasto_total * 100).round(1)
mejor_camp    = df.loc[df["roi_pct"].idxmax()]
peor_camp     = df.loc[df["roi_pct"].idxmin()]
horas_ahorradas = 12  # estimación de automatización

print(f"  Gasto total invertido    : ${gasto_total:,.0f}")
print(f"  Revenue total generado   : ${revenue_total:,.0f}")
print(f"  ROI global               : {roi_global}%")
print(f"  Mejor campaña            : {mejor_camp['nombre_campana']} ({mejor_camp['roi_pct']}% ROI)")
print(f"  Campaña a revisar        : {peor_camp['nombre_campana']} ({peor_camp['roi_pct']}% ROI)")
print(f"  Horas de reporte ahorradas/mes: {horas_ahorradas}hs (automatización)")
print("=" * 60)


# ─────────────────────────────────────────────────────────
# 6. EXPORTAR ARCHIVOS
# ─────────────────────────────────────────────────────────
df.to_csv("../data/campanas_limpias.csv", index=False)
funnel.to_csv("../data/funnel_plataforma.csv", index=False)

# JSON para Grafana
grafana_data = []
for _, r in df.iterrows():
    grafana_data.append({
        "campana": r["nombre_campana"],
        "plataforma": r["plataforma"],
        "roi": float(r["roi_pct"]),
        "ctr": float(r["ctr_pct"]),
        "cpl": float(r["cpl"]),
        "conversiones": int(r["conversiones"]),
        "gasto": float(r["gasto_real"]),
        "estado": r["estado"]
    })

with open("../grafana/metricas_grafana.json", "w", encoding="utf-8") as f:
    json.dump(grafana_data, f, ensure_ascii=False, indent=2)

print(f"\n✔ Archivos exportados:")
print(f"   → data/campanas_limpias.csv   (para Power BI)")
print(f"   → data/funnel_plataforma.csv  (para Power BI - Funnel)")
print(f"   → grafana/metricas_grafana.json (para Grafana datasource)")

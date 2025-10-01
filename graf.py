import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================
# CONFIGURACIÓN INICIAL
# ============================
os.makedirs("graficas", exist_ok=True)

# Leer el dataset
df = pd.read_csv("estilovida.csv")

# Convertir columnas relevantes a numéricas
cols_numeric = [
    "Sunshine hours(City)",
    "Happiness levels(Country)",
    "Obesity levels(Country)",
    "Life expectancy(years) (Country)",
    "Outdoor activities(City)"
]
for c in cols_numeric:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# ============================
# 1. Sunshine hours vs Happiness
# ============================

# Aseguramos que las columnas sean numéricas
df["Happiness levels(Country)"] = pd.to_numeric(df["Happiness levels(Country)"], errors="coerce")
df["Sunshine hours(City)"] = pd.to_numeric(df["Sunshine hours(City)"], errors="coerce")

# Agrupamos por nivel de felicidad y calculamos el promedio de horas de sol
df_sun_happy = (
    df.groupby("Happiness levels(Country)")["Sunshine hours(City)"]
      .mean()
      .reset_index()
      .sort_values("Happiness levels(Country)")
)

# Gráfico de líneas
plt.figure(figsize=(10,6))
sns.lineplot(
    data=df_sun_happy,
    x="Happiness levels(Country)",
    y="Sunshine hours(City)",
    marker="o",
    color="darkorange"
)
plt.title("Promedio de Horas de Sol y Nivel de Felicidad")
plt.xlabel("Nivel de felicidad (1-10)")
plt.ylabel("Promedio de horas de sol (Horas)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("graficas/sol_vs_felicidad_linea.png")
plt.close()


# ============================
# 2. Happiness levels by Country (Top 10)
# ============================

# Agrupamos por país y calculamos el promedio de felicidad
df_happiness = (
    df.groupby("City")["Happiness levels(Country)"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
sns.barplot(x=df_happiness.values, y=df_happiness.index, palette="Blues_r")
plt.title("Top 10 Ciudades Felices")
plt.xlabel("Happiness level (0-10)")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("graficas/felicidad_top10.png")
plt.close()



# ============================
# 3. Promedio de horas de sol por ciudad
# ============================

# Aseguramos que la columna sea numérica
df["Sunshine hours(City)"] = pd.to_numeric(df["Sunshine hours(City)"], errors="coerce")

# Agrupamos por ciudad y calculamos el promedio
df_sun = (
    df.groupby("City")["Sunshine hours(City)"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
sns.barplot(x=df_sun.index, y=df_sun.values, palette="YlOrBr")
plt.title("Promedio de Horas de Sol por Ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Horas de sol (promedio)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("graficas/horas_sol_ciudades.png")
plt.close()


# ============================
# 4. Outdoor activities vs Happiness
# Aseguramos que las columnas sean numéricas
df["Happiness levels(Country)"] = pd.to_numeric(df["Happiness levels(Country)"], errors="coerce")
df["Outdoor activities(City)"] = pd.to_numeric(df["Outdoor activities(City)"], errors="coerce")

# Agrupamos por nivel de felicidad y calculamos el promedio de actividades al aire libre
df_outdoor_happy = (
    df.groupby("Happiness levels(Country)")["Outdoor activities(City)"]
      .mean()
      .reset_index()
      .sort_values("Happiness levels(Country)")
)

# Gráfico de líneas
plt.figure(figsize=(10,6))
sns.lineplot(
    data=df_outdoor_happy,
    x="Happiness levels(Country)",
    y="Outdoor activities(City)",
    marker="o",
    color="seagreen"
)
plt.title("Promedio de Actividades al Aire Libre según Nivel de Felicidad")
plt.xlabel("Nivel de felicidad (1-10)")
plt.ylabel("Promedio de actividades al aire libre")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("graficas/actividades_vs_felicidad_linea.png")
plt.close()





print("✅ Gráficas generadas y guardadas en la carpeta 'graficas/'")
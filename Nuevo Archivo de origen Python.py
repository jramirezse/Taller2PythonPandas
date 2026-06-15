import pandas as pd
import os


def clasificar_apreciacion(calificacion):
    if calificacion > 8.5:
        return "Excelente"
    elif calificacion >= 7.0:
        return "Buena"
    elif calificacion >= 5.0:
        return "Regular"
    elif calificacion >= 3.0:
        return "Mala"
    else:
        return "Pesima"


def main():
    ruta_entrada = "input/peliculas.csv"
    carpeta_salida = "output"

    os.makedirs(carpeta_salida, exist_ok=True)

    df = pd.read_csv(ruta_entrada)

    peliculas_transformadas = df[["titulo", "genero", "calificacion"]].copy()

    peliculas_transformadas["clasica"] = df["anio"] < 1995

    peliculas_transformadas["apreciacion"] = df["calificacion"].apply(
        clasificar_apreciacion
    )

    peliculas_transformadas.to_csv(
        "output/peliculas_transformadas.csv",
        index=False
    )

    analisis_generos = df.groupby("genero").agg(
        promedio_calificacion=("calificacion", "mean"),
        cantidad_peliculas=("titulo", "count")
    ).reset_index()

    analisis_generos.to_excel(
        "output/analisis_generos.xlsx",
        index=False
    )

    print("Archivo CSV generado: output/peliculas_transformadas.csv")
    print("Archivo Excel generado: output/analisis_generos.xlsx")


if __name__ == "__main__":
    main()
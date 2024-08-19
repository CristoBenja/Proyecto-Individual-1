import pandas as pd

df_movies = pd.read_csv("Movies_ETL.csv")
df_movies["release_date"] = pd.to_datetime(df_movies["release_date"])
df_movies["mes"] = df_movies["release_date"].dt.month

meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}

def cantidad_filmaciones_mes(mes):
    
    try:
        mes = str(mes).lower()
        if mes not in meses:
            raise ValueError("Mes inválido. Por favor, escribir un mes válido.")
    except ValueError as e:
        print(e)
    else:
        mes_num = meses[mes]
        total_peliculas_mes = df_movies[df_movies["mes"] == mes_num].shape[0]
        print(f"Cantidad de filmaciones en el mes de {mes}: {total_peliculas_mes}")


cantidad_filmaciones_mes("enero")
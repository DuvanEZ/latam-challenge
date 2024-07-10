from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Abrir y leer el archivo JSON línea por línea
    with open(file_path, 'r') as json_file:
        data = [json.loads(line.strip()) for line in json_file]

    # Extraer los campos necesarios si están presentes en el item
    data = [
        (item['date'], item['user']['username'], item['id']) 
        for item in data 
        if 'date' in item and 'user' in item and 'id' in item and 'username' in item['user']
    ]

    # Crear un DataFrame de pandas con los datos extraídos
    df = pd.DataFrame(data, columns=['date', 'user', 'id'])
    
    # Convertir el campo 'date' a formato datetime.date
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Agrupar por fecha y contar los tweets, luego seleccionar las 10 fechas con más tweets
    tweet_counts = df.groupby('date').size()
    top_10_dates = tweet_counts.nlargest(10).index.tolist()

    # Encontrar el usuario más frecuente para cada una de las 10 fechas con más tweets
    top_users = (
        df[df['date'].isin(top_10_dates)]
        .groupby('date')['user']
        .agg(lambda x: x.mode()[0] if not x.empty else None)
        .reindex(top_10_dates)  # Asegurar el orden correcto de las fechas
    )

    # Convertir el resultado en una lista de tuplas (fecha, usuario más frecuente)
    result = list(top_users.items())
    
    return result
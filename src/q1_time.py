from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    with open(file_path, 'r') as json_file:
        #Cargar archivo json linea a linea
        data = [json.loads(line.strip()) for line in json_file]
    #Usar una list comprenhension para extraer los campos
    data = [(item['date'], item['user']['username'], item['id']) for item in data if 'date' in item and 'user' in item and 'id' in item and 'id' in item['user']]

    #Convertir la lista de tuplas en un dataframe de pandas
    df = pd.DataFrame(data, columns=['date', 'user', 'id'])
    
    # Convertir campo date en formato datetime
    df['date'] = pd.to_datetime(df['date']).dt.date

    tweet_counts = df.groupby('date').size()
    top_10_dates = tweet_counts.nlargest(10).index
    df_top_10 = df[df['date'].isin(top_10_dates)]
    top_users = df_top_10.groupby('date')['user'].agg(lambda x: x.value_counts().index[0])

    # Convertir el resulatado en una lista de tuplas
    result = [(date, user) for date, user in zip(top_10_dates, top_users)]
    
    return result
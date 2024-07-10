# Challenge de Eficiencia en Memoria y Tiempo

En este repositorio se completa el challenge compuesto por 3 preguntas donde se busca obtener una solución *memory efficient* y una solución *time efficient* para cada una de las preguntas. Las preguntas son:

## 1. Las top 10 fechas donde hay más tweets

Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días. Debe incluir las siguientes funciones:

```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
  [(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
  [(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
```

## 2. Los top 10 emojis más usados con su respectivo conteo
Debe incluir las siguientes funciones: 
```
def q2_time(file_path: str) -> List[Tuple[str, int]]:
def q2_memory(file_path: str) -> List[Tuple[str, int]]:

Returns:
[("✈️", 6856), ("❤️", 5876), ...]
```

## 3. El top 10 histórico de usuarios (username) más influyentes

En función del conteo de las menciones (@) que registra cada uno de ellos. Debe incluir las siguientes funciones
```
def q3_time(file_path: str) -> List[Tuple[str, int]]:
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
Returns:
[("LATAM321", 387), ("LATAM_CHI", 129), ...]
```
## Explicación
Dentro de la carpeta src se podrán encontrar las funciones fuentes encargadas para cada una de las preguntas. Adicionalmente, hay un archivo llamado challenge.ipynb donde se utilizan funcionalidades extras para determinar la mejora en memoria y tiempo.

Cabe aclarar que dentro del archivo challenge.ipynb se incluyó código hecho en Spark para el primer punto, esto con el fin de mostrar que es una solución perfecta cuando hablamos de escalabilidad y rapidez, pero esta solución no se tomó para la solución mostrada por el main.py ya que requiere de más librerías y un montaje más complejo.
## Archivos principales
Se elaboraron dos soluciones finales: una está hecha con Flask, ya que nos proporciona facilidad en el manejo de APIs y conexiones; esta solución es con la que se generó un contenedor de Docker. Tenemos otra solución final usando Streamlit, la cual es una solución más visual y agradable, pero para esta se requiere poder de cómputo más grande y una solución más elaborada.
# Imagen de lo obtenido en flask con una imagen montada desde docker
![Alt text](subdirectory/Flask_app.png)

# Imagenes Streamlit
Question 1
![Alt text](subdirectory/streamlit_question.png)
Question 2
![Alt text](subdirectory/streamlit_question2.png)
Question 3
![Alt text](subdirectory/streamlit_question3.png)


## Consideraciones
Adicional, cabe aclarar que este proyecto fue hecho por una persona natural con sus limitaciones en la cantidad de plataformas que se puedan usar y/o recursos. En caso tal de querer una solución totalmente escalable y habilitada en cualquier parte, lo mejor sería realizar un montaje en nube donde la fuente de datos provenga ya sea de un bucket o otra fuente accesible y considerar la posibilidad de usar servicios de nube como lo puede ser BigQuery para elaborar una solución warehouse donde la rapidez de procesamiento es clara. 







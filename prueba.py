from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
app.title="Mi aplicacion con FastAPI MOVIES JED"
app.version="0.0.1"
movies_list = [
    {
        "id": 1,
        "title": "Annihilation",
        "año": 2018,
        "director": "Alex Garland",
        "overview": "ciencia ficción de 2018. Un grupo de sobrevivientes de una operación secreta se prepara para la invasión alieni",
    },
        {
            "id": 2,
            "title": "Parasites",
            "año": 2019,
            "director": "Bong Joon-ho",
            "overview": "Historia familia de 4 miembros que se infiltra a base de mentiras como empleados domesticos"
        }
]
@app.get('/', tags=["Home"])
def message():
    #return 'Bootcamp Programacion Python 2024 132'
    return HTMLResponse('<h1>Hello World/h1>')

@app.get('/movies/{id}', tags = ["Movies"])
def get_movies(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []
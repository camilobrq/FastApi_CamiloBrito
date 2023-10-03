from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/interes-simple")
def calcular_interes_simple(principal: float, tasa: float, tiempo: float):
    # Realiza el cálculo de interés simple aquí
    interes = principal * (tasa / 100) * tiempo
    return {"interes_simple": interes}

@app.get("/interes-compuesto")
def calcular_interes_compuesto(principal: float, tasa: float, tiempo: float):
    # Realiza el cálculo de interés compuesto aquí
    interes = principal * (1 + tasa / 100) ** tiempo - principal
    return {"interes_compuesto": interes}
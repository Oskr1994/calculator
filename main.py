from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numeros(BaseModel):
    num1: float
    num2: float

@app.get("/")
def read_root():
    return {"mensaje": "Hola, Bienvenido a mi calculadora"}

@app.post("/sumar")
def sumar(numeros: Numeros):
    resultado = numeros.num1 + numeros.num2
    return {"resultado": resultado}

@app.post("/restar")
def restar(numeros: Numeros):
    resultado = numeros.num1 - numeros.num2
    return {"resultado": resultado}

@app.post("/multiplicar")
def restar(numeros: Numeros):
    resultado = numeros.num1 * numeros.num2
    return {"resultado": resultado}

@app.post("/dividir")
def restar(numeros: Numeros):
    resultado = numeros.num1 / numeros.num2
    return {"resultado": resultado}
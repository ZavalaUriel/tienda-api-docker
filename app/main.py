import socket

from fastapi import FastAPI, HTTPException

VERSION = "1.0.0"

app = FastAPI(title="API Tienda", version=VERSION)


def calcular_precio(precio: float, descuento: float) -> float:
    if precio < 0:
        raise ValueError("Precio invalido")
    if not 0 <= descuento <= 100:
        raise ValueError("Descuento invalido")
    return precio * (1 - descuento / 100)


def calcular_iva(precio: float) -> float:
    return precio * 1.16


@app.get("/")
def inicio():
    return {
        "mensaje": "API de la tienda en Docker",
        "version": VERSION,
        "contenedor": socket.gethostname(),
    }


@app.get("/salud")
def salud():
    return {"estado": "ok"}


@app.get("/precio")
def precio(precio: float, descuento: float = 0):
    try:
        subtotal = calcular_precio(precio, descuento)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    return {
        "precio": precio,
        "descuento": descuento,
        "subtotal": round(subtotal, 2),
        "total_con_iva": round(calcular_iva(subtotal), 2),
    }

import pytest
from fastapi.testclient import TestClient

from app.main import app, calcular_iva, calcular_precio

client = TestClient(app)


def test_calcular_precio_con_descuento():
    assert calcular_precio(200, 25) == 150


def test_calcular_precio_sin_descuento():
    assert calcular_precio(80, 0) == 80


def test_calcular_precio_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_precio(200, 150)


def test_calcular_iva():
    assert calcular_iva(100) == pytest.approx(116)


def test_endpoint_inicio():
    respuesta = client.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json()["version"] == "1.0.0"


def test_endpoint_salud():
    respuesta = client.get("/salud")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"estado": "ok"}


def test_endpoint_precio():
    respuesta = client.get("/precio", params={"precio": 200, "descuento": 25})
    assert respuesta.status_code == 200
    assert respuesta.json()["total_con_iva"] == 174.0


def test_endpoint_precio_invalido():
    respuesta = client.get("/precio", params={"precio": 200, "descuento": 150})
    assert respuesta.status_code == 400
    assert respuesta.json()["detail"] == "Descuento invalido"

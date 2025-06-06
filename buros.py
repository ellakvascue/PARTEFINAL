import random

def consulta_buro(curp):
    if random.choice([True, False]):
        return {"estatus": "Encontrado", "detalle": [{"año": 2023, "score": random.randint(500, 850)}]}
    return {"estatus": "Sin historial"}

def consulta_circulo(curp):
    if random.choice([True, False]):
        return {"estatus": "Encontrado", "detalle": [{"año": 2022, "score": random.randint(500, 850)}]}
    return {"estatus": "Sin historial"}

def consulta_titan(curp):
    if random.choice([True, False]):
        return {"estatus": "Encontrado", "detalle": [{"año": 2024, "score": random.randint(500, 850)}]}
    return {"estatus": "Sin historial"}

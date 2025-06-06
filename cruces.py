import sqlite3
import pandas as pd

def generar_prospectos_cruces():
    # Simulación de generación de prospectos desde cruces
    prospectos = [
        {"nombre": "Juan", "paterno": "Perez", "materno": "Lopez", "ciudad": "CDMX", "estado": "Ciudad de México"},
        {"nombre": "Maria", "paterno": "Gomez", "materno": "Hernandez", "ciudad": "Guadalajara", "estado": "Jalisco"},
        {"nombre": "Luis", "paterno": "Martinez", "materno": "Ramirez", "ciudad": "Monterrey", "estado": "Nuevo León"},
    ]
    return prospectos

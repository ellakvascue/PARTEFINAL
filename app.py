print("INICIANDO APP.PY CORRECTO")
from flask import Flask, request, jsonify
from modules.renapo import consulta_renapo
from modules.buros import consulta_buro, consulta_circulo, consulta_titan
from datetime import datetime

app = Flask(__name__)

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.json
    nombre = data.get("nombre", "")
    paterno = data.get("paterno", "")
    materno = data.get("materno", "")

    resultados_renapo = consulta_renapo(nombre, paterno, materno)

    filtrados = []
    for persona in resultados_renapo:
        fnac = datetime.strptime(persona["fecha_nacimiento"], "%Y-%m-%d")
        edad = 2025 - fnac.year
        if edad > 23 or (edad == 23 and fnac.month < 6):
            buro = consulta_buro(persona["curp"])
            circulo = consulta_circulo(persona["curp"])
            titan = consulta_titan(persona["curp"])
            filtrados.append({
                "nombre": persona["nombre"],
                "paterno": persona["paterno"],
                "materno": persona["materno"],
                "fecha_nacimiento": persona["fecha_nacimiento"],
                "curp": persona["curp"],
                "buro": buro,
                "circulo": circulo,
                "titan": titan
            })
    return jsonify(filtrados)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)

from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

RENAPO_API_URL = "https://api.renapo.gob.mx/curp"

@app.route('/api/renapo/search', methods=['POST'])
def search_homonimos():
    try:
        data = request.json
        nombre = data.get('nombre', '')
        apellido_paterno = data.get('apellidoPaterno', '')
        apellido_materno = data.get('apellidoMaterno', '')

        if not nombre or not apellido_paterno or not apellido_materno:
            return jsonify({"error": "Datos incompletos"}), 400

        response = requests.post(RENAPO_API_URL, json={
            "nombre": nombre,
            "apellidoPaterno": apellido_paterno,
            "apellidoMaterno": apellido_materno
        })

        if response.status_code != 200:
            logging.error(f"Error en la API de RENAPO: {response.status_code}")
            return jsonify({"error": "Error en la API de RENAPO"}), 500

        results = response.json()
        filtered_results = [
            r for r in results if int(r['fechaNacimiento'].split('-')[0]) <= 2002
        ]

        return jsonify(filtered_results)
    except Exception as e:
        logging.error(f"Error inesperado: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)

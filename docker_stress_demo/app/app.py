from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

#Configuración básica desde variables de entorno
STRESS_SECONDS = int(os.getenv("STRESS_SECONDS", "5"))
STRESS_INTENSITY = int(os.getenv("STRESS_INTENSITY", "10_000_000"))


@app.route("/")
def index():
    """
    Endpoint para comprobar que la app responde.
    """
    return jsonify(
        status="ok",
        message="Stress app funcionando",
        hostname=os.uname().nodename if hasattr(os, "uname") else "desconocido",
    )


@app.route("/stress-cpu")
def stress_cpu():
    """
    Se encarga de simular carga de CPU durante "STRESS_SECONDS" segundos.
    """
    start = time.time()
    iterations = 0

    while time.time() - start < STRESS_SECONDS:
        iterations += 1
        _ = STRESS_INTENSITY * STRESS_INTENSITY

    return jsonify(
        status="ok",
        message=f"CPU estresada durante ~{STRESS_SECONDS} segundos",
        iterations=iterations,
    )


@app.route("/crash")
def crash():
    """
    Endpoint que simula un fallo fatal de la app.
    Termina el proceso de forma inmediata.
    """
    os._exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

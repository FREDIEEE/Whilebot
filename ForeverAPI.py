from time import sleep, time, localtime,strftime
from flask import Flask, request, jsonify
from waitress import serve
import threading
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(message)s')

web_server = Flask(__name__)

@web_server.route("/download", methods=["GET"])
def testret():
    return jsonify({"response": "HELLO WORLD "})

def hilo_server():
    while True:
        serve(web_server, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
        sleep(5)

def hilo_time():
    while True:
        TimeNow = strftime("%H:%M:%S", localtime())
        print(f"ALF_API: Corriendo servidor x tiempo {TimeNow}")
        sleep(320) #Cada 5 min


if __name__ == "__main__":
    print(os.environ)
    print("ALF_API: Iniciando servicio infinito")
    hilo = threading.Thread(name="hilo_webhook", target=hilo_time)
    hilo.start()
    hilo2 = threading.Thread(name="hilo_webhook", target=hilo_server)
    hilo2.start()
    while True:
        sleep(1)
        TimeNow = strftime("%H:%M:%S", localtime())

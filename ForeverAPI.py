from time import sleep, time, localtime,strftime
import threading
import logging
import os
import sys

global USERS
logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(message)s')

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
    while True:
        sleep(1)
        TimeNow = strftime("%H:%M:%S", localtime())

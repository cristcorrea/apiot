
from machine import Pin, Timer, unique_id
import dht
import time
import json
import ubinascii
from collections import OrderedDict
from settings import SERVIDOR_MQTT
from umqtt.robust import MQTTClient

CLIENT_ID = ubinascii.hexlify(unique_id()).decode('utf-8')

mqtt = MQTTClient(CLIENT_ID, SERVIDOR_MQTT,
                  port=8883, keepalive=10, ssl=True)

led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))
contador = 0

bandera = True

def heartbeat(nada):
    global contador
    if contador > 5:
        pulsos.deinit()
        contador = 0
        return
    led.value(not led.value())
    contador += 1
  
def transmitir():
    print("publicando")
    mqtt.connect()
    mqtt.publish(f"ap/{CLIENT_ID}",datos)
    mqtt.disconnect()

while True:
    try:
        temp_max = 26
        temp_min = 22
        d.measure()
        temperatura = d.temperature()
        humedad = d.humidity()
        if (temperatura > temp_max) and bandera:
            datos = json.dumps(OrderedDict([
            ('temperatura',temperatura),
            ('humedad',humedad)
             ]))
            transmitir()
            bandera = False
            print(datos)
        elif temperatura < temp_min:
            bandera = True   
    except OSError as e:
        print("sin sensor")
    time.sleep(5)

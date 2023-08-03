

from machine import Pin, Timer
import dht
import time
import json
from collections import OrderedDict

sw = Pin(23, Pin.IN)
led = Pin(22, Pin.OUT)
d = dht.DHT22(Pin(21))
print("esperando pulsador")
contador = 0
estado = False
temperatura_total = 0
humedad_total = 0

def alternar(pin):
    global contador, estado, temperatura_total, humedad_total

    if sw.value():
        if not estado:
            contador += 1
            if contador == 1:
                d.measure()
                temperatura_total = d.temperature()
                humedad_total = d.humidity()
            else:
                d.measure()
                temperatura_total += d.temperature()
                humedad_total += d.humidity()

                media_temperatura = temperatura_total / contador
                media_humedad = humedad_total / contador

                datos = json.dumps(OrderedDict([
                    ('temperatura', media_temperatura),
                    ('humedad', media_humedad)
                ]))
                print(datos)
                contador = 0

        estado = True
    else:
        estado = False

timer1 = Timer(1)
timer1.init(period=50, mode=Timer.PERIODIC, callback=alternar)

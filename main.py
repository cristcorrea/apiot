# Cristian Correa
# Ejercicio 2 APIOT 2023

from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador = 0

while True:
    while sw.value():
        contador += 1
        time.sleep_ms(1)
    if 200 < contador < 400:
        print("pulsacion corta")
        contador = 0
    elif contador > 600:
        print("pulsacion larga")
        contador = 0
    else:
        contador = 0

# Cristian Correa
# Ejercicio 1 APIOT 2023

from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador = 0

while True:
    if sw.value():
        contador += 1
        print(contador)
    if contador == 10:
        print("enciende led")
        led.value(not led.value())
        contador = 0
    time.sleep_ms(200)

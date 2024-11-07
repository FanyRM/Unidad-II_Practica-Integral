#Imports para led y tiempo 
from machine import Pin
from time import sleep

#Variables para botón y led
led = Pin(4, Pin.OUT)
bTog = Pin(16, Pin.IN, Pin.PULL_UP) 


#Estado del led
led_state = False

#Difino función que intercale el encendido y apagado
def toggle(pin):
    global led_state
    led_state = not led_state
    led.value(led_state)

#Instrucción que se lanza despúes de presionar el botón
bTog.irq(trigger=Pin.IRQ_FALLING, handler=toggle)

while True:
    pass
    
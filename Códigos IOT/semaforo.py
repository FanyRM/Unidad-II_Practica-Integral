from machine import Pin, time_pulse_us
import time

# Definir pines
PIN_TRIG = Pin(15, Pin.OUT)
PIN_ECHO = Pin(4, Pin.IN)
led_rojo = Pin(27, Pin.OUT)
led_verde = Pin(25, Pin.OUT)
led_amarillo = Pin(26, Pin.OUT)

# Función para medir la distancia
def medir_distancia():
    # Generar pulso de disparo
    PIN_TRIG.off()
    time.sleep_us(2)
    PIN_TRIG.on()
    time.sleep_us(10)
    PIN_TRIG.off()
    
    # Medir duración del pulso de eco
    duracion = time_pulse_us(PIN_ECHO, 1, 30000)  # Tiempo límite de 30ms para evitar bloqueos
    distancia = (duracion / 58.0) if duracion > 0 else -1  # Convertir a cm si la medición es válida
    return distancia

while True:
    distancia = medir_distancia()
    print("Distancia en CM:", distancia)
    
    # Control de los LEDs según la distancia
    if distancia > 18:
        # Luz verde
        led_verde.on()
        led_amarillo.off()
        led_rojo.off()
    elif 10 < distancia <= 18:
        # Luz amarilla
        led_verde.off()
        led_amarillo.on()
        led_rojo.off()
    elif 3 < distancia <= 10:
        # Luz roja
        led_verde.off()
        led_amarillo.off()
        led_rojo.on()
    elif distancia <= 3 and distancia != -1:
        # Luz roja para advertencia más cercana
        led_verde.off()
        led_amarillo.off()
        led_rojo.on()

    # Pausa de 500 ms antes de la siguiente medición
    time.sleep(1)

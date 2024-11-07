from machine import Pin, time_pulse_us
from time import sleep
from machine import PWM
from hcsr04 import HCSR04
from servo import Servo
import time

# Configuramos el sensor hcsr04 en el pin 15
PIN_TRIG = Pin(15, Pin.OUT)
PIN_ECHO = Pin(4, Pin.IN)

# Configuramos el servo en el pin 4
servo_pin = Pin(2)
servo = PWM(servo_pin, freq=50)

# Función para mover el servo a un ángulo específico
def move_servo(angle):
    duty = 40 + int((angle / 180) * 115)
    servo.duty(duty)
    
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
    try:
        # Leemos los valores del sensor

        # Si la humedad es mayor a 50, movemos el servo a 90 grados
        distancia = medir_distancia()
        print("Distancia en CM:", distancia)
    
        # Control de los LEDs según la distancia
        if distancia > 10:
            move_servo(90)
        else:
            move_servo(0)

        sleep(1)
    except OSError as e:
        print("Error al leer el sensor:", e)
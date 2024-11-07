from machine import Pin
from time import sleep
import dht
from machine import PWM

# Configuramos el sensor DHT11 en el pin 15
sensor = dht.DHT11(Pin(15))

# Configuramos el servo en el pin 4
servo_pin = Pin(4)
servo = PWM(servo_pin, freq=50)

# Función para mover el servo a un ángulo específico
def move_servo(angle):
    duty = 40 + int((angle / 180) * 115)
    servo.duty(duty)

while True:
    try:
        # Leemos los valores del sensor
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        print("humedad:", h)

        # Si la humedad es mayor a 50, movemos el servo a 90 grados
        if h > 70:
            move_servo(90)
        else:
            move_servo(0)

        sleep(1)
    except OSError as e:
        print("Error al leer el sensor:", e)
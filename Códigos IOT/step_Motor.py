import uasyncio as asyncio
from hcsr04 import HCSR04
from servo import Servo
from machine import Pin, PWM
from time import sleep_ms

# Definición de sensor
sensor = HCSR04(15, 4, 24000)
# Definicion led
led_rojo = Pin(2, Pin.OUT)
led_2 = Pin(25, Pin.OUT)
# Definir servos
servoPatas = Servo(Pin(12))
servoCabez = Servo(Pin(13))

# Definir notas para el buzzer
B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 441
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 710
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978
REST = 0

navireggae = [
    G5, G5, F5, E5, D5, E5, F5, G5,  # "Feliz Navidad"
    D5, E5, F5, D5, E5, F5, D5, C5,  # "próspero año y felicidad"
    G5, E5, D5, F5, E5, G5, F5, D5,  # Melodía intermedia reguetón
    C5, D5, G4, F4, G4, F4, E4, D4,  # "Alegría para todos"
    D5, F5, G5, E5, D5, C5, G4, G5,  # Estribillo de reguetón
    G5, G5, G5, REST, G5, G5, G5, REST,    # Intro rítmica
    F5, F5, REST, E5, D5, REST, F5, F5,    # "Feliz Navidad"
    G5, G5, F5, E5, D5, REST, E5, F5,      # Continuación
    G5, REST, D5, E5, F5, REST, D5, C5,    # "próspero año y felicidad"
    G5, REST, E5, E5, D5, D5, REST, F5,    # Ritmo intermedio reguetón
    G5, REST, F5, F5, D5, D5, REST, C5,    # Más ritmo
    D5, REST, G4, REST, F4, REST, G4, F4,  # "Alegría para todos"
    E4, REST, D4, REST, D5, REST, F5, REST, # Estribillo
    
]

class Buzzer:
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin))  # Asegúrate de usar el pin correcto
        self.pwm.freq(1000)

    async def play(self, melody, wait, duty):
        for note in melody:
            if note == REST:
                self.pwm.duty(0)
            else:
                self.pwm.freq(note)
                self.pwm.duty(duty)
                led_rojo.value(1)
                led_2.value(1)
                await asyncio.sleep_ms(wait // 2)
                led_rojo.value(0)
                led_2.value(0)
            await asyncio.sleep_ms(wait)
        self.pwm.duty(0)

# Instanciar el objeto Buzzer
buzzer = Buzzer(14)

async def mover_servos():
    while True:
        servoPatas.move(180)
        servoCabez.move(180)
        await asyncio.sleep(2)
        servoPatas.move(0)
        servoCabez.move(0)
        await asyncio.sleep(2)

async def main():
    while True:
        distancia = sensor.distance_cm()
        if distancia <= 15:
            led_rojo.value(1)
            led_2.value(1)
            # Ejecutar el buzzer y el movimiento de los servos en paralelo
            await asyncio.gather(buzzer.play(navireggae, 150, 512), mover_servos())
        else:
            led_rojo.value(0)
            led_2.value(0)
            servoCabez.move(0)
            servoPatas.move(0)
        await asyncio.sleep(2)

# Ejecutar el bucle principal
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Programa detenido")
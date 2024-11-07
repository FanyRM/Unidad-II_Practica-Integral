import machine
import neopixel
import framebuf
import time

# Configuración del potenciómetro
pot = machine.ADC(machine.Pin(32))
pot.atten(machine.ADC.ATTN_11DB)  # Ajustar el rango del ADC para lecturas de 0 a 3.3V

# Configuración de la matriz NeoPixel
PIN = 2  # Pin de datos de los NeoPixels
NUM_LEDS = 64  # 8x8 matriz tiene 64 LEDs

# Inicializa los LEDs
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

# Definir las dimensiones de la matriz
ancho = 8
alto = 8

# Crear un buffer para el framebuffer (1 bit por píxel)
buffer = bytearray(ancho * alto // 8)

# Inicializar framebuffer en modo monocromático (1 bit por píxel)
fb = framebuf.FrameBuffer(buffer, ancho, alto, framebuf.MONO_HLSB)

# Función para encender los LEDs según el framebuffer
def encender_leds(color):
    for x in range(ancho):
        for y in range(alto):
            # Obtener el valor del píxel (1 si está encendido, 0 si está apagado)
            valor = fb.pixel(x, y)

            # Calcular la posición del LED en la matriz en modo zigzag por columnas
            if x % 2 == 0:  # Columnas pares (de arriba a abajo)
                index = x * alto + y
            else:  # Columnas impares (de abajo a arriba)
                index = x * alto + (alto - 1 - y)

            # Encender el LED si el píxel está encendido, con el color definido
            if valor:
                np[index] = color  # Usar el color definido
            else:
                np[index] = (0, 0, 0)  # Apagar el LED
    np.write()  # Actualizar los LEDs

# Función para calcular el porcentaje del potenciómetro
def obtener_porcentaje_pot():
    valor_pot = pot.read()  # Leer el valor del ADC (0 a 4095)
    porcentaje = int((valor_pot / 4095) * 100)  # Calcular el porcentaje
    return porcentaje

# Función para mostrar el porcentaje desplazándose si no cabe
def mostrar_porcentaje(porcentaje):
    fb.fill(0)  # Limpiar framebuffer
    texto = "{}%".format(porcentaje)  # Formatear el texto del porcentaje
    texto_largo = len(texto) * 8  # Longitud total del texto en píxeles (8 píxeles por carácter)
    
    desplazamiento = 0  # Desplazamiento inicial
    while desplazamiento < texto_largo - ancho + 1:  # Mientras el texto no esté completamente mostrado
        fb.fill(0)  # Limpiar framebuffer antes de dibujar
        fb.text(texto, -desplazamiento, 0, 1)  # Dibujar el texto con desplazamiento
        
        encender_leds((255, 67, 12))  # Usar color azul para mostrar el texto
        desplazamiento += 1  # Mover el texto un píxel hacia la izquierda
        time.sleep(0.1)  # Ajustar la velocidad de desplazamiento

# Bucle principal
while True:
    porcentaje = obtener_porcentaje_pot()  # Obtener el porcentaje del potenciómetro
    mostrar_porcentaje(porcentaje)  # Mostrar el porcentaje en la matriz LED
    time.sleep(0.5)  # Actualizar cada 500 ms
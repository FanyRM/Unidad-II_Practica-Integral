import machine
import neopixel
import framebuf
import time

# Configuración de la matriz NeoPixel
PIN = 14  # Pin de datos de los NeoPixels
NUM_LEDS = 256  # 32x8 matriz tiene 256 LEDs

# Inicializa los LEDs
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

# Definir las dimensiones de la matriz
ancho = 8
alto = 8

# Crear un buffer para el framebuffer (1 bit por píxel)
buffer = bytearray(ancho * alto // 8)

# Inicializar framebuffer en modo monocromático (1 bit por píxel)
fb = framebuf.FrameBuffer(buffer, ancho, alto, framebuf.MONO_HLSB)

# Función para generar los colores de la bandera de México
def generar_color(t):
    # Alternar entre los colores verde, blanco y rojo
    if t % 3 == 0:
        return (235, 70, 139)  # ROSA
    elif t % 3 == 1:
        return (255, 255, 255)  # BLANCO
    else:
        return (142, 0, 59)  # ROSA CLARO

# Función para encender los LEDs según el framebuffer
def encender_leds(t):
    color = generar_color(t)  # Cambiar el color entre verde, blanco y rojo
    for x in range(ancho):
        for y in range(alto):
            # Obtener el valor del píxel (1 si está encendido, 0 si está apagado)
            valor = fb.pixel(x, y)

            # Calcular la posición del LED en la matriz en modo zigzag por columnas
            if x % 2 == 0:  # Columnas pares (de arriba a abajo)
                index = x * alto + y
            else:  # Columnas impares (de abajo a arriba)
                index = x * alto + (alto - 1 - y)

            # Encender el LED si el píxel está encendido, con el color dinámico
            if valor:
                np[index] = color  # Usar el color verde, blanco o rojo
            else:
                np[index] = (0, 0, 0)  # Apagar el LED
    np.write()  # Actualizar los LEDs

# Mantener el desplazamiento continuo sin cortes
def desplazamiento_continuo(texto):
    desplazamiento = 0
    t = 0
    texto += " "  # Añadir un espacio para la separación continua
    texto_largo = len(texto) * 8  # Longitud total del texto en píxeles
    while True:  # Bucle infinito para hacer que el desplazamiento sea continuo
        # Redibujar el texto completo, de manera continua y sin cortes
        fb.fill(0)  # Limpiar framebuffer antes de dibujar
        
        # Dibujar dos veces el texto para evitar cortes entre el final y el principio
        fb.text(texto, -desplazamiento, 0, 1)
        fb.text(texto, texto_largo - desplazamiento, 0, 1)
        
        encender_leds(t)
        
        desplazamiento += 1  # Mover el texto un píxel hacia la izquierda
        if desplazamiento >= texto_largo:  # Reiniciar el desplazamiento
            desplazamiento = 0
        t += 1  # Incrementar el tiempo para alternar colores
        
        time.sleep(0.08)  # Ajustar la velocidad de desplazamiento

# Iniciar el desplazamiento continuo con el texto "HOLA MUNDO"
texto = "Celeste Guapa"
desplazamiento_continuo(texto)
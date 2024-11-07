#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Definiciones para el tamaño de la pantalla OLED
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// Configuración del pin del potenciómetro
int potPin = 32;  // El pin analógico donde está conectado el potenciómetro

// Configuración de la pantalla OLED
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  // Inicializar el serial para depuración
  Serial.begin(9600);

  // Comenzar la pantalla OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Dirección I2C de la pantalla OLED
    Serial.println(F("Error al inicializar el display OLED"));
    for (;;);
  }

  // Limpiar la pantalla para asegurarse de que no quede basura
  display.clearDisplay();
}

void drawTank(int x, int y, int width, int height, int fill_percentage) {
  // Dibujar el contorno del tanque
  display.drawRect(x, y, width, height, SSD1306_WHITE);

  // Calcular la altura del llenado
  int fillHeight = (fill_percentage / 100.0) * height;

  // Dibujar el llenado del tanque
  display.fillRect(x + 1, y + height - fillHeight, width - 2, fillHeight, SSD1306_WHITE);
}

void loop() {
  // Leer el valor del potenciómetro (rango de 0 a 1023)
  int valor = analogRead(potPin);

  // Convertir el valor a porcentaje (0 a 100%)
  int porcentaje = map(valor, 0, 1023, 0, 100);

  // Limpiar la pantalla
  display.clearDisplay();

  // Dibujar el tanque en el centro de la pantalla
  drawTank(50, 10, 28, 44, porcentaje);

  // Mostrar el porcentaje de llenado
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(50, 55);
  display.print(porcentaje);
  display.print('%');

  // Actualizar la pantalla
  display.display();

  // Esperar un momento antes de leer nuevamente
  delay(100);
}

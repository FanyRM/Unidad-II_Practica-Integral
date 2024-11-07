#include <ESP32Servo.h> // Importamos la librería del servo

int button = 4; // Pin al que está conectado el botón
Servo servo;    // Instancia del servo

void setup() {
  servo.attach(25);     // Conectar el servo al pin 25
  pinMode(button, INPUT_PULLUP); // Configurar el pin del botón como entrada con resistencia pull-up interna
}

void loop() {
  int buttonState = digitalRead(button); // Leer el estado del botón

  if (buttonState == LOW) {  // Si el botón está presionado (estado LOW con PULLUP)
    servo.write(180);         // Mover el servo a 90 grados
  } else {
    servo.write(0);          // Mover el servo a 0 grados cuando el botón no está presionado
  }

  delay(10); // Pequeña pausa para evitar rebotes
}

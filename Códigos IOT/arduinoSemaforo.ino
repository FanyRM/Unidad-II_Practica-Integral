#define PIN_TRIG 15
#define PIN_ECHO 4

int led_rojo = 27;
int led_verde = 25;
int led_amarillo = 26;

void setup() {
  Serial.begin(115200);

  // Configurar pines para el sensor ultrasónico
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);

  // Configurar pines para los LEDs
  pinMode(led_rojo, OUTPUT); 
  pinMode(led_verde, OUTPUT); 
  pinMode(led_amarillo, OUTPUT); 
}

void loop() {
  // Iniciar nueva medición
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);

  // Leer el resultado del sensor ultrasónico
  long duration = pulseIn(PIN_ECHO, HIGH);
  float distancia = duration / 58.0;  // Convertir la duración a distancia en cm

  Serial.print("Distancia en CM: ");
  Serial.println(distancia);

  // Lógica del semáforo basada en distancias de 18 cm, 10 cm y 3 cm
  if (distancia > 18) {
    // Si la distancia es mayor a 18 cm - Luz verde
    digitalWrite(led_verde, HIGH);
    digitalWrite(led_rojo, LOW);
    digitalWrite(led_amarillo, LOW);
  } else if (distancia <= 18 && distancia > 10) {
    // Si la distancia es entre 10 cm y 18 cm - Luz amarilla
    digitalWrite(led_verde, LOW);
    digitalWrite(led_amarillo, HIGH);
    digitalWrite(led_rojo, LOW);
  } else if (distancia <= 10 && distancia > 3) {
    // Si la distancia es entre 3 cm y 10 cm - Luz roja
    digitalWrite(led_verde, LOW);
    digitalWrite(led_amarillo, LOW);
    digitalWrite(led_rojo, HIGH);
  } else if (distancia <= 3) {
    // Si la distancia es menor o igual a 3 cm - Luz roja (mayor advertencia)
    digitalWrite(led_verde, LOW);
    digitalWrite(led_amarillo, LOW);
    digitalWrite(led_rojo, HIGH);
  }

  delay(500);  // Esperar 500 ms antes de la siguiente medición
}

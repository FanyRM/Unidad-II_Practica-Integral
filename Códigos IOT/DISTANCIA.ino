// Definir pines
const int PIN_TRIG = 15; // Pin de disparo
const int PIN_ECHO = 4;  // Pin de eco
const int LED_ROJO = 27; 
const int LED_VERDE = 25;
const int LED_AMARILLO = 26;

void setup() {
  // Inicializar los pines de los LEDs como salida
  pinMode(LED_ROJO, OUTPUT);
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_AMARILLO, OUTPUT);
  
  // Inicializar los pines del sensor ultrasonico
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  
  // Inicializar la comunicación serial para monitoreo
  Serial.begin(9600);
}

// Función para medir la distancia
long medir_distancia() {
  // Generar pulso de disparo
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);
  
  // Medir la duración del pulso de eco
  long duracion = pulseIn(PIN_ECHO, HIGH, 30000);  // Limitar el tiempo de espera a 30 ms
  
  // Calcular la distancia en cm
  long distancia = (duracion > 0) ? (duracion / 58.0) : -1;
  return distancia;
}

void loop() {
  long distancia = medir_distancia();
  Serial.print("Distancia en CM: ");
  Serial.println(distancia);
  
  // Control de los LEDs según la distancia
  if (distancia > 18) {
    digitalWrite(LED_VERDE, HIGH);
    digitalWrite(LED_AMARILLO, LOW);
    digitalWrite(LED_ROJO, LOW);
  } else if (distancia > 10 && distancia <= 18) {
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_AMARILLO, HIGH);
    digitalWrite(LED_ROJO, LOW);
  } else if (distancia > 3 && distancia <= 10) {
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_AMARILLO, LOW);
    digitalWrite(LED_ROJO, HIGH);
  } else if (distancia <= 3 && distancia != -1) {
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_AMARILLO, LOW);
    digitalWrite(LED_ROJO, HIGH);
  }

  // Pausa de 500 ms antes de la siguiente medición
  delay(500);
}

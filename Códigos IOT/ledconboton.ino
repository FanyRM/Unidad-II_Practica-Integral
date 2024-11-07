int led1=4;
int led2=25;
int bOn1=27;
int bOn2=18;


//Declaro el estado del led
bool state = false;

void setup() {
  // Iniciamos pines para botones y led
  pinMode(led1, OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(bOn1,INPUT_PULLUP);
  pinMode(bOn2, INPUT_PULLUP);
  
}

void loop() {
  // Lecturas digitales para los botones
  if(digitalRead(bOn1)==LOW){
    if(state){
      
      digitalWrite(led1,LOW);
      state = false;
    }else{
      digitalWrite(led1, HIGH);
          state=true;
    }
    while(digitalRead(bOn1)==LOW){}
    }

    if(digitalRead(bOn2)==LOW){
      if(state){
        digitalWrite(led2, LOW);
        state= false;
        }else{
          digitalWrite(led2, HIGH);
          state=true;
        }
        while(digitalRead(bOn2)== LOW){}

      }
}
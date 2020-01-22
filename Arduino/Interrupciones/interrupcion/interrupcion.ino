#define ledPin 13
#define interruptPin 2
#define interruptPin2 3
volatile byte state = LOW;
volatile byte state2 = LOW;
unsigned int incomingByte = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(interruptPin, INPUT_PULLUP);
  pinMode(interruptPin2, INPUT_PULLUP);
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, CHANGE);
  attachInterrupt(digitalPinToInterrupt(interruptPin2), blink2, RISING);
}

void loop() {  
  digitalWrite(ledPin, state);
  incomingByte = Serial.read();
  if(incomingByte == 115)
  {
    Serial.print("Estado de la puerta: ");
    if(state)
    {
      Serial.print("abierta - "); 
      Serial.print(state);       
      Serial.print("\n"); 
    }    
    else
    {
      Serial.print("cerrada - "); 
      Serial.print(state);       
      Serial.print("\n"); 
    }
    Serial.print("Estado de la chapa: ");
    if(!state2)
    {
      Serial.print("conectada - "); 
      Serial.print(state2);       
      Serial.print("\n"); 
    }    
    else
    {
      Serial.print("desconectada - "); 
      Serial.print(state2);       
      Serial.print("\n"); 
    }
  }
}

void blink()
{
 static unsigned long last_interrupt_time = 0;
 unsigned long interrupt_time = millis();
 if (interrupt_time - last_interrupt_time > 20)
 {
   state = !state;  
   while(Serial.available() > 0) {
    Serial.print(state); 
   }
 }
 last_interrupt_time = interrupt_time;      
}

void blink2()
{
 static unsigned long last_interrupt_time2 = 0;
 unsigned long interrupt_time2 = millis();
 if (interrupt_time2 - last_interrupt_time2 > 10)
 {
   state2 = !state2;     
   while(Serial.available() > 0) {
    Serial.print(state2);
   }
 }
 last_interrupt_time2 = interrupt_time2;       
}

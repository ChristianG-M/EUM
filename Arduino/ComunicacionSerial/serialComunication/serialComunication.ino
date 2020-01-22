String incomingByte = "";

void setup() {
  Serial.begin(9600);
}

void loop() {  
  if (Serial.available() > 0) {    
    incomingByte = Serial.readString();
    
    Serial.print("I received: ");
    Serial.print(incomingByte);
  }
}

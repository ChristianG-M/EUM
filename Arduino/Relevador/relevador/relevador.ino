#define salidaRele 7
#define pushButton 11
#define ledPlaca LED_BUILTIN
int statusButton = 0;

void setup() 
{
  pinMode(salidaRele, OUTPUT);
  pinMode(pushButton, INPUT);
  pinMode(ledPlaca, OUTPUT);
}

void loop() 
{    
  statusButton = digitalRead(pushButton);
  if(statusButton == HIGH)
  {
    digitalWrite(salidaRele, HIGH);
    digitalWrite(ledPlaca, HIGH);
  }
  else
  {
    digitalWrite(salidaRele, LOW);
    digitalWrite(ledPlaca, LOW);
  }
}

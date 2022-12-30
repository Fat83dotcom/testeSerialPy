#include <Arduino.h>
int recebeNum;


void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

int contador = 0;

void loop() {
  // Serial.println("*****************");
  if (Serial.available() > 0){
    recebeNum = Serial.read();
    digitalWrite(LED_BUILTIN, 1);
    if (recebeNum == 'u'){
      Serial.print("u ");
      Serial.println(92.7745, 3);
      digitalWrite(LED_BUILTIN, 0);
    }
    if (recebeNum == 'p'){
      Serial.print("p ");
      Serial.println(956.9965, 3);
      digitalWrite(LED_BUILTIN, 0);
    }
    if (recebeNum == '1'){
      Serial.print("1 ");
      Serial.println(23.9912, 3);
      digitalWrite(LED_BUILTIN, 0);
    }
    if (recebeNum == '2'){
      Serial.print("2 ");
      Serial.println(21.8787, 3);
      digitalWrite(LED_BUILTIN, 0);
    }
    // Serial.println("-----------------------");
  }
  
  digitalWrite(LED_BUILTIN, 0);
}
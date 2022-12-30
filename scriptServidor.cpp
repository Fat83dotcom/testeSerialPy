#include <Arduino.h>

void setup() {
  Serial.begin(9600);
}

int bytesRecebidos;

void loop() {
  if (Serial.available() > 0){
    bytesRecebidos = Serial.read();
    digitalWrite(LED_BUILTIN, 1);
    if (bytesRecebidos == 'u'){
      Serial.print("u ");
      Serial.println(92.7745, 3);
    }
    if (bytesRecebidos == 'p'){
      Serial.print("p ");
      Serial.println(956.9965, 3);
    }
    if (bytesRecebidos == '1'){
      Serial.print("1 ");
      Serial.println(23.9912, 3);
    }
    if (bytesRecebidos == '2'){
      Serial.print("2 ");
      Serial.println(21.8787, 3);
    }
  }
}
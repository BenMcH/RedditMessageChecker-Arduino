char chara = 0;
void setup(){
 Serial.begin(9600);
 pinMode(13, OUTPUT);
}

void loop(){
 if (Serial.available() > 0) {
    chara = Serial.read();
    digitalWrite(13, chara=='1'?HIGH:LOW);
  } 
}

#define BUZZER 8

void setup() {
  Serial.begin(9600);
}


void loop() {

  if (Serial.available()) {

    String data = Serial.readStringUntil('\n');


    int comma = data.indexOf(',');


    int frequency = data.substring(0, comma).toInt();

    int duration = data.substring(comma + 1).toInt();


    if(frequency > 0){
      tone(BUZZER, frequency, duration);
    }
    else{
      noTone(BUZZER);
    }


    delay(duration);
  }
}
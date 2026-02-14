#include <Wire.h>
#include <Adafruit_SSD1306.h>

#define RELAY_PIN 4
#define SAFETY_SWITCH 7
#define BUZZER 9

Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {
  Serial.begin(9600);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(SAFETY_SWITCH, INPUT_PULLUP);
  pinMode(BUZZER, OUTPUT);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
}

void runSterilization(int seconds) {
  for(int i = seconds; i > 0; i--) {
    // CRITICAL SAFETY CHECK
    if(digitalRead(SAFETY_SWITCH) == HIGH) { // Door Opened
      digitalWrite(RELAY_PIN, LOW);
      Serial.println("ABORTED");
      return;
    }
    
    digitalWrite(RELAY_PIN, HIGH);
    // Update OLED countdown
    delay(1000);
  }
  digitalWrite(RELAY_PIN, LOW);
  tone(BUZZER, 1000, 500);
  Serial.println("Completed");
}

void loop() {
  // Wait for button press to start cycle
}

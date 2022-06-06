#include "ESPControl.h"

const int pushbuttons[] = { D0, D1, D2, D3 };
const int indicator = D6;

#define SSID "wifi-ssid"
#define PASS "wifi-password"

const String id = "1234567";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  start(SSID, PASS);

  for (int x : pushbuttons)
  {
    pinMode(x, INPUT);
  }

  pinMode(indicator, OUTPUT);
  digitalWrite(indicator, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  // wait for requests
  waitUntilNewReq();

  String bits = "";
  for (int i = 0; i < 4; i++)
  {
    // reads each button
    // char reading = (digitalRead(pushbuttons[i])) ? 't' : 'f';
    int reading = digitalRead(pushbuttons[i]);
    bits += String(reading);
  }

  // construct data
  String data = id + "$" + bits;
  Serial.print("Sending ");
  Serial.println(data);

  // send data to python
  returnThisStr(data);
}

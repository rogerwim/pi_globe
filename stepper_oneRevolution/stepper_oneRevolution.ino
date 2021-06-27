
/*
 Stepper Motor Control - one revolution

 This program drives a unipolar or bipolar stepper motor.
 The motor is attached to digital pins 8 - 11 of the Arduino.

 The motor should revolve one revolution in one direction, then
 one revolution in the other direction.


 Created 11 Mar. 2007
 Modified 30 Nov. 2009
 by Tom Igoe

 */
#include <Stepper.h>
float rot = 0.0;
const int stepsPerRevolution = 1440;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
int home() {
  if(analogRead(A0) > 0) {
    return 0;  
  }
  int count = 0;
  while(analogRead(A0) < 10) {
    myStepper.step(1);
    count++;
  }
  return count;
}
void step2() {
  long ang = 360;
  long steps = ang/(360/stepsPerRevolution);
  Serial.println(steps);
  myStepper.step(steps);
}
void stop() {
  digitalWrite(8,0);
  digitalWrite(9,0);
  digitalWrite(10,0);
  digitalWrite(11,0);
}
void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(7);
  // initialize the serial port:
  Serial.begin(9600);
  home();
}

void loop() {
  // step one revolution  in one direction:
  //int a = home();
  //if(a != 0) {
  //  Serial.println(a);  
  //}
  step2();
  delay(1000);
  //stop();
}

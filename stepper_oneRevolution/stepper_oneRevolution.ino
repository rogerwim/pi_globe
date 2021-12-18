
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
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

  // attaches the servo on pin 9 to the servo object

float rot = 0.0;
const float stepsPerRevolution = 1540.0;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
void home() {

  while(analogRead(A0) < 500) {
    myStepper.step(1);

  }

}
void goto_ang(long steps) {
  home();
  myStepper.step(steps);
}
void step2(long steps) {
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
  myservo.attach(6);
  // initialize the serial port:
  Serial.begin(9600);
  home();
  stop();
}
int command, num1,num2;
long steps;
void loop() {
  // step one revolution  in one direction:
  if (Serial.available() >= 8) { // COMMAND,UNUSED,DATA,DATA,UNUSED,UNUSED,UNUSED,UNUSED
  
  command = Serial.read();
  Serial.read();
  num1 = Serial.read();
  num2 = Serial.read();
  Serial.read();
  Serial.read();
  Serial.read();
  Serial.read();
  if(command & 3) {
    steps = num1*256+num2;
    if((command & 1) > 0) {
      goto_ang(steps);
      stop();
    }
    if((command & 2) > 0) {
      step2(steps);
      stop();
    }
  }
  if((command & 4) > 0) {
    home();
    stop();
  }
  if((command & 8) > 0) {
    myservo.write(num2);
  }
  Serial.write(255);
  }
}

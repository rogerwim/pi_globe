// pins 8 through 11 stepper control
// pin 7 laser
// pin 6 servo
// pin A0 reed switch


#include <Stepper.h>
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

float rot = 0.0;
const float stepsPerRevolution = 1440.0;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
long long count = 0;
long long rev = 0;
bool r;
void fake_home() {

  while(true) {
    myStepper.step(1);
    count++;
    if(analogRead(A0) > 500 and not r) {
      r = true;
      rev++;
    } else if(analogRead(A0) < 500) {
      r = false;
    }
    if(count % 100 == 0) {
    Serial.print((long)rev);
    Serial.print(" ");
    Serial.print((long)count);
    Serial.print(" ");
    Serial.println((float)count/(float)rev);
    }
    }

  }

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
  myStepper.setSpeed(12);
  myservo.attach(6);
  // initialize the serial port:
  Serial.begin(9600);
  home();
  stop();
  pinMode(7,OUTPUT);
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
  if((command & 16) > 0) {
    if(num2) {
      digitalWrite(7,HIGH);
    } else {
      digitalWrite(7,LOW);
    }
  }
  Serial.write(255);
  }
}

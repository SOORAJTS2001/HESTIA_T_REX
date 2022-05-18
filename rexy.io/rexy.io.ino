/*int x;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 Serial.print(x + 1);
}*/
#include <Servo.h>
int x;
Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards
int  prevval = 0;
int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  while (!Serial.available());
  int currval = Serial.readString().toInt();
  if(currval>prevval)
  {
    for(int i = prevval;i<=currval;i++)
    {
      myservo.write(i);
    }
  }
  else if(currval<prevval)
  {
    for(int i = prevval;i>=currval;i--)
    {
      myservo.write(i);
    }
  }
  prevval = currval;
 
                // tell servo to go to position in variable 'pos'
  delay(1000);                       // waits 15ms for the servo to reach the position
  
}

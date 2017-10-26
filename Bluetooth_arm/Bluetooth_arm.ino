#include<Servo.h>

//Variable for storing received data
char data = 0;   

//Servos
Servo servo_grabber;
Servo servo_swivel;
Servo servo_wrist;
Servo servo_elbow;
Servo servo_shoulder;
Servo servo_base;

Servo servos [6] = {servo_grabber,servo_swivel,servo_wrist,servo_elbow,servo_shoulder,servo_base};

String command;

//loop counter
int i;
//store the position from the passed data
int location;

void setup()
{
  //Sets the baud for serial data transmission  
  Serial.begin(9600);  

  //Set up servo pins for output
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
     
  //Servo pins for servo control
  servo_grabber.attach(2);
  servo_swivel.attach(3);
  servo_wrist.attach(4);
  servo_elbow.attach(5);
  servo_shoulder.attach(6);
  servo_base.attach(7);

  servo_grabber.write(10);
  servo_swivel.write(120);
  servo_wrist.write(15);
  servo_elbow.write(120);
  servo_shoulder.write(35);
  servo_base.write(150);

}

void loop()
{
    while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (inChar != 'L' || inChar != '\'' || inChar != 'b') {
      // convert the incoming byte to a char and add it to the string:
      command += (char)inChar;
    }
    // if you get a newline, print the string, then the string's value:
    else if(inChar == 'L' || inChar == '\n')
    break;
      
    
  }

    //Move grabber to the postition recieved from 
    if(command[0] == 'g')
    {
      location = command.substring(1).toInt();
      servo_grabber.write(location);
    }
    if(command.substring(0,2) == "sw")
    {
      location = command.substring(2).toInt();
      servo_swivel.write(location);
    }
    if(command[0] == 'w')
    {
      location = command.substring(1).toInt();
      servo_grabber.write(location);
    }
    if(command[0] == 'e')
    {
      location = command.substring(1).toInt();
      servo_grabber.write(location);
    }
    if(command.substring(0,2) == "sh"){
      location = command.substring(2).toInt();
      servo_shoulder.write(location);
    }
    if(command[0] == 't')
    {
      location = command.substring(1).toInt();
      servo_grabber.write(location);
    }
    if(command == "reset"){
      
      //loop through the servos to reset them all
      servo_grabber.write(0);
    }
  command = " ";
  }




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


//commands for servos
//arm up, down, buttons released
//Y up, A down
String grabber_commands[] = {"b21","b01","b20","b00"};

//claw open, claw close, buttons released
//Left bumper open, Right bumper close
String swivel_commands[] = {"b51","b41","b50","b40"};

//ramp up, ramp down, buttons released
//Left trigger up, Right trigger down
String wrist_commands[] = {"ty8","tx8"};

String elbow_commands[] = {"ey8","ex8"}; // temp commands

//base up, base down, buttons released
//Left joystick up, Left joystick down
String shoulder_commands[] = {"y-6","y+6"};

//joints up, joints down, buttons released
//Right joystick up, Right joystick down
String base_commands[] = {"r-6","r+6"};

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
}

void loop()
{
    while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (inChar != 'L' ) {
      // convert the incoming byte to a char and add it to the string:
      command += (char)inChar;
      //Serial.println(command);
    }
    // if you get a newline, print the string, then the string's value:
    if(inChar == 'L'){
      break;   
    }
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
    if(command[0] == 'b')
    {
      location = command.substring(1).toInt();
      servo_grabber.write(location);
    }
    if(command == "reset"){
      //loop through the servos to reset them all
    }
  command = " ";
  }




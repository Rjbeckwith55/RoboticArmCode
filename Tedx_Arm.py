import serial
import pygame

#control update frequency
CLOCK = pygame.time.Clock()
clock_speed = 20

pygame.init()

#vars for if program running
#and if joystick connected
joystick_connect = True
running = True

#use first joystick connected since only
#one xbox remote is used
joystick = pygame.joystick.Joystick(0)
#initailize joystick
joystick.init()

#initialize the serial connection with the Arduino
ser = serial.Serial('COM7',9600)

#increment variables
start_pos = [-15, 120, 15, 120, 35, 150]
servo_pos = [-15, 120, 15, 120, 35, 150]
command = ['g','sw','w','e','sh','b']
#string for concatinating the commmand
text = " "

#BOOOLS for movement
base_mv = False
base_mv_opp = False
shoulder_mv = False
shoulder_mv_opp = False
elbow_mv = False
elbow_mv_opp = False
swivel_mv = False
swivel_mv_opp = False
wrist_mv = False
wrist_mv_opp = False
gripper_mv = False
gripper_mv_opp = False

#increment amounts
b_mv = 3
s_mv = 5
e_mv = 5
sw_mv = 5
w_mv = 5
g_mv = 5

def stop():
    data = "offL"
    ser.write(data.encode())
    pygame.quit()
    print('clean exit')
    
def reset():
    data = "ResetL"
    data.encode(data.encode())
    ser.write(data)
             
pygame.init()


#run until user decides to quit
while(running):
    # User did something, this applies to keyboard or
    #joystick
    for event in pygame.event.get(): 
        base_mv = False
        base_mv_opp = False
        shoulder_mv = False
        shoulder_mv_opp = False
        elbow_mv = False
        elbow_mv_opp = False
        swivel_mv = False
        swivel_mv_opp = False
        wrist_mv = False
        wrist_mv_opp = False
        gripper_mv = False
        gripper_mv_opp = False
        # Check if anything on joystick changed   
        if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYAXISMOTION:

            #Control swivel base
            #Top left axis, left direction
            #does not allow user to go past limits
            if joystick.get_axis(0) > .9:
                base_mv = True
            elif joystick.get_axis(0) < -.9:
                base_mv_opp = True
            else:
                base_mv = False
                base_mv_opp = False

            #Shoulders - left stick, up/down
            if joystick.get_axis(1) < -.9:
                shoulder_mv = True
            elif joystick.get_axis(1) > .9:
                shoulder_mv_opp = True
            else:
                shoulder_mv = False
                shoulder_mv_opp = False

            #elbow - right stick, up/down
            if joystick.get_axis(4) < -.5:
                elbow_mv = True
            elif joystick.get_axis(4) > .5:
                elbow_mv_opp = True
            else:
                elbow_mv = False
                elbow_mv_opp = False

            #wrist joint - A and Y, A down Y up
            if joystick.get_button(0):
                swivel_mv = True
            elif joystick.get_button(3):
                swivel_mv_opp = True
            else:
                swivel_mv = False
                swivel_mv_opp = False
                

            #wrist swivel - RB and LB, RB left (CCW) LB right (CW)
            if joystick.get_button(5):
                wrist_mv = True
            elif joystick.get_button(4):
                wrist_mv_opp = True
            else:
                wrist_mv = False
                wrist_mv_opp = False

            #gripper - Left trigger open, right trigger close
            if joystick.get_axis(2) > .5:
                gripper_mv = True
            elif joystick.get_axis(2) < -.5:
                gripper_mv_opp = True
            else:
                gripper_mv = False
                gripper_mv_opp = False
            
            #exit program if start button pressed
            if joystick.get_button(7):
                running = False
                
    #move base
    if base_mv and servo_pos[0] <= 100:
        #increase the position of the servo by the amount of movement
        servo_pos[0] += b_mv
        #concatinate the string all together and add an L to the end so
        #the Arduino can tell when the end of the command is
        data = command[0] + str(servo_pos[0]) +"L"
        print(data)
        ser.write(data.encode())
    elif base_mv_opp and servo_pos[0] >= -15:
        servo_pos[0] -= b_mv
        data = command[0] + str(servo_pos[0])+"L"
        print(data)
        ser.write(data.encode())

    #Shoulders - left stick, up/down
    if shoulder_mv and servo_pos[1] <= 130:
        servo_pos[1] += s_mv
        data = command[1] + str(servo_pos[1])+"L"
        print(data)
        ser.write(data.encode())
    elif shoulder_mv_opp and servo_pos[1] >= 0:
        servo_pos[1] -= s_mv
        data = command[1] + str(servo_pos[1])+"L"
        print(data)
        ser.write(data.encode())

    #elbow - right stick, up/down
    if elbow_mv and servo_pos[2] <= 100:
        servo_pos[2] += e_mv
        data = command[2] + str(servo_pos[2])+"L"
        print(data)
        ser.write(data.encode())
    elif elbow_mv_opp and servo_pos[2] >= 0:
        servo_pos[2] -= e_mv
        data = command[2] + str(servo_pos[2])+"L"
        print(data)
        ser.write(data.encode())

    #wrist joint - A and Y, A down Y up
    if swivel_mv and servo_pos[3] <= 170:
        servo_pos[3] += sw_mv
        data = command[3] + str(servo_pos[3])+"L"
        print(data)
        ser.write(data.encode())
    elif swivel_mv_opp and servo_pos[3] >= 10:
        servo_pos[3] -= sw_mv
        data = command[3] + str(servo_pos[3])+"L"
        print(data)
        ser.write(data.encode())

    #wrist swivel - RB and LB, RB left (CCW) LB right (CW)
    if wrist_mv and servo_pos[4] <= 180:
        servo_pos[4] += w_mv
        data = command[4] + str(servo_pos[4])+"L"
        print(data)
        ser.write(data.encode())
    elif wrist_mv_opp and servo_pos[4] >= 0:
        servo_pos[4] -= w_mv
        data = command[4] + str(servo_pos[4])+"L"
        print(data)
        ser.write(data.encode())

    #gripper - Left trigger open, right trigger close
    if gripper_mv and servo_pos[5] <= 170:
        servo_pos[5] += g_mv
        data = command[5] + str(servo_pos[5])+"L"
        print(data)
        ser.write(data.encode())
    elif gripper_mv_opp and servo_pos[5] >= 0:
        servo_pos[5] -= g_mv
        data = command[5] + str(servo_pos[5])+"L"
        print(data)
        ser.write(data.encode())

    
    #set clock speed to limit cpu usage
    CLOCK.tick(clock_speed)
    
#end program
stop()


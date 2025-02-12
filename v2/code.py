print("loading libs")
import board
import time
from joystick_xl.inputs import Axis, Button
from joystick_xl.joystick import Joystick

print("input init")
joystick = Joystick()

joystick.add_input(
    Axis(board.A1),
    Axis(board.A0),
    Button(board.GP0),
    Button(board.GP2),
    Button(board.GP3),
    Button(board.GP4),
    Button(board.GP5),
    Button(board.GP6),
    Button(board.GP7),
    Button(board.GP8),
    Button(board.GP9),
    Button(board.GP10),
    Button(board.GP11),
    Button(board.GP12),
    Button(),
    Button(),
    
    Button(),
    Button(),
    
    Button(),
    Button(),
)

print("begin main loop")
while True:


    if joystick.button[4].was_pressed:
        print("key just toggled ON")
        #joystick.button[12].source_value = False

    if joystick.button[4].was_released:
        print("key just toggled OFF")
        #joystick.button[12].source_value = True

    #MAP one toggle to two buttons
    if joystick.button[0].was_pressed:
        joystick.button[0].bypass = True
        joystick.button[16].source_value = False

    if joystick.button[0].was_released:
        joystick.button[0].bypass = True
        joystick.button[17].source_value = False
    
    
    #MAP one toggle to two buttons
    if joystick.button[5].was_pressed:
        joystick.button[5].bypass = True
        joystick.button[12].source_value = False

    if joystick.button[5].was_released:
        joystick.button[5].bypass = True
        joystick.button[13].source_value = False
        
   #MAP one toggle to two buttons
    if joystick.button[6].was_pressed:
        joystick.button[6].bypass = True
        joystick.button[14].source_value = False

    if joystick.button[6].was_released:
        joystick.button[6].bypass = True
        joystick.button[15].source_value = False


    #ignition lockout, green button does not work without key being on
    if joystick.button[4].is_pressed:
        joystick.button[2].bypass = False      
    if not joystick.button[4].is_pressed:   
        joystick.button[2].bypass = True
        #print("ignition lockout")
    
    #nitrous lockout, red button does not work without key being on
    if joystick.button[5].is_pressed:
        joystick.button[3].bypass = True      
    if not joystick.button[5].is_pressed:   
        joystick.button[3].bypass = False
        #print("nitrous lockout")

    i = 0
    while i < len(joystick.button):
        if joystick.button[i].was_pressed:
            print("button just pressed: " + str(i))
        i = i + 1

    #send HID packet to PC
    joystick.update()
    
    #clear virtual buttons back to not-pressed (HIGH)
    joystick.button[12].source_value = True
    joystick.button[13].source_value = True
    joystick.button[14].source_value = True
    joystick.button[15].source_value = True
    joystick.button[16].source_value = True
    joystick.button[17].source_value = True

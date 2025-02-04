import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# define buttons. these can be any physical switches/buttons, but the values
toggle1 = digitalio.DigitalInOut(board.GP0)
toggle1.pull = digitalio.Pull.UP
toggle2 = digitalio.DigitalInOut(board.GP1)
toggle2.pull = digitalio.Pull.UP
toggle3 = digitalio.DigitalInOut(board.GP2)
toggle3.pull = digitalio.Pull.UP

button1 = digitalio.DigitalInOut(board.GP7)
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP8)
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.GP9)
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.GP10)
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.GP11)
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.GP12)
button6.pull = digitalio.Pull.UP

toggle1State = 0
toggle2State = 0
toggle3State = 0

while True:
    
#if the toggle/button is used, press the corresponding key
#each toggle switch corresponds to two keys, for its two states, on/off
    if toggle1.value != toggle1State:
        toggle1State = toggle1.value
        if toggle1.value:
            kbd.send(Keycode.F13)
        if not toggle1.value:
            kbd.send(Keycode.F14)

    if toggle2.value != toggle2State:
        toggle2State = toggle2.value
        if toggle2.value:
            kbd.send(Keycode.F15)
        if not toggle2.value:
            kbd.send(Keycode.F16)

    if toggle3.value != toggle3State:
        toggle3State = toggle3.value
        if toggle3.value:
            kbd.send(Keycode.F17)
        if not toggle3.value:
            kbd.send(Keycode.F18)

#buttons correspond to a keypress/release
#since they are switching ground, "not" value = pressed
    if not button1.value:
        kbd.press(Keycode.F19)
    if button2.value:
        kbd.release(Keycode.F19)

    if not button2.value:
        kbd.press(Keycode.F20)
    if button2.value:
        kbd.release(Keycode.F20)

    if not button3.value:
        kbd.press(Keycode.F21)
    if button3.value:
        kbd.release(Keycode.F21)

    if not button4.value:
        kbd.press(Keycode.F22)
    if button4.value:
        kbd.release(Keycode.F22)

    if not button5.value:
        kbd.press(Keycode.F23)
    if button5.value:
        kbd.release(Keycode.F23)

    if not button6.value:
        kbd.press(Keycode.F24)
    if button6.value:
        kbd.release(Keycode.F24)
    #...continue this until all are mapped
    

    time.sleep(0.1)

# rpi-pico2-simpanel
An open-source button box for simulator use.

STL files are from [TinkerCAD](https://www.tinkercad.com).  Links to Tinker This! option are including in the 3d printing section of this document.

**Introduction**

I play a lot of racing games, but also a lot of one specific game, [BeamNG.drive](https://store.steampowered.com/app/284160/BeamNGdrive/).  Less of a racing sim and more of a vehicular physics sandbox, it offers the ability to free roam large worlds in a variety of vehicles.  From a 4x4 "Go-Devil" powered Jeep type vehicle to a 400 horsepower hatchback with nitrous, the open nature of gameplay in BeamNG provides a need for many control bindings.  I found over the years that I frequently used a specific few key bindings, and that putting down a gamepad or reaching over the steering wheel to hit a keyboard key is... not as fun as mashing a button or flicking a switch. 

A friend mentioned that they had an arduino-based button box in their sim rig, and I thought "hey, I could build that, I know arduino and basic electronics".  Then I ordered the wrong arduino boards, did some research and ordered rpi-pico2 boards instead.  It might be overkill for a dozen keys worth of functionality, but if it works and it works reliably without having to sort through knockoffs and bad variants of the board... well, then it's better.  Just order your rpi pico or pico2 board from a reputable retailer like [Mouser](https://www.mouser.com/) or [Adafruit](https://www.adafruit.com/) and you'll be fine.  

**3d Printing or "Making a box with holes in it"**

The case is 3d printable.  So if you have a home manufactury machine of some variety (or have a friend who does) you should be able to make your own box.  Alternatively you could order a suitable size project box or enclosure from any number of electronics component retailers... again, Mouser or Adafruit are the first two places *I* would look.

I have designed this to be printed easily on pretty much any FDM machine.  The box face is completely flat, and should print as the model is oriented, face-down.  This ensures a nice surface finish on the face you're going to look at most.  I recommend printing it with enough walls and top/bottom layers to make the case basically solid plastic.  This ensures that your mounting points do not become loose over time as infill begins to crack from repeated stress.

The box can be printed in PLA, ABS, PETG, weedeater line, or whatever else you feed your FDM machine.  Before committing to a 6 hour or more print to make a nice sturdy box, it's worthwhile to print the test-part first to ensure that you have the right size holes to snugly fit your switches of choice.

Test-Fit Model: 
- [Tinker This!](https://www.tinkercad.com/things/ilWKCudVXyv/edit?returnTo=%2Fdashboard&sharecode=KZdAHi8J1aMUUtoJdOfRdpk8CTP9DpqL5B3aQJiVsnA)
- Filename: test_fit.stl

This small part allows test-fitting two different size switches.  Adjust and export in TinkerCAD as needed, the switches I used were two different sizes for toggles and momentary buttons... yours may be different.  Once you have confirmed a good fit for your switches, make the needed adjustments to the holes in the TinkerCAD design for the box and export to STL/print.  Ungrouping the completed design ONCE will detach the holes, which are a group of their own.  Ungrouping these will allow you to adjust position and size.

Button-Box Model:
- [Tinker This!](https://www.tinkercad.com/things/5mHoQv5xTlQ-buttonbox/edit?returnTo=https%3A%2F%2Fwww.tinkercad.com%2Fdashboard&sharecode=nY8Vci4_1xVKrHl18sUt108QHbWfSm0StkJ5l9jJreM)
- Filename: button_box.stl

Again, the design is intended to print face-down on a glass or patterned bed.  This will help ensure the front panel of your button box looks nice.  The labels adjacent to the button box in CAD are examples of printable labels that can be glued on with a dab of CA (superglue).  You can print these multi-material by pausing/swapping filament, or with a multi-material machine.  You can also print them in a single material and paint the letters in a contrasting color with a paint pen, as I did.

**Electronics or "How does a plastic box with switches become a gamepad?"**

I had originally planned to build this using an Arduino or ATMEL-based microcontroller.  If you are unfamiliar with these, they are little circuit boards about the size of a stick of gum that you program over USB, and solder what I call "electronic goodies" to, and make stuff.  They can make flashy lights, set off stage effects, work as a gamepad, control a hobby robot, etc etc etc.  There is a problem, the Arduino space in hobby electronics is almost flooded with knockoff boards.  Some are good, some are meh, and some are outright bad.  But for around $5, you can have a tiny 8-bit computer that you make do nifty things.  

After ordering a few, and learning upon arrival that they had "knockoff" parts on the board, I then decided to go with a somewhat newer ecosystem, the rpi pico.  From what research I did, I was able to identify that these are perfectly capable of performing HID duty, or "Human Interface Device".  Meaning they can be a gamepad or keyboard.  

In the example, we'll be programming this rpi pico board to be a keyboard with 12 keys.  This then begs the question, what keys do they press?  Well, we're going to use keys that don't typically exist on keyboard.  At the top of your keyboard, you should have F1 through F12.  The function-keys.  Did you know most computers support F13 through F24 as well?  They're not on most keyboards, because we don't need them... but here, we can make our buttons be those unused keys and then set the control bindings in our game to respond to these new keys.  Instead of thinking of the button box as a keyboard, perhaps think of it as a keyboard extension.

Now, your rpi-pico board should be wired to switch ground.  Meaning you want to connect your switches and buttons between GND or electrical ground, and the IO pins.  Each switch should connect to ground and an IO pin.  You may (if you have many buttons/switches) find that a bit of perfboard works to create a ground bus.  This will permit connecting many switches to a single ground pin on the rpi pico board.  I hear some of you asking "what the heck is ground?  you mean the floor?"  Well, electrically speaking, there is voltage... or potential.  In this case the board runs at five (5) volts (V).  There is also the opposite of that, to put it simply, which is ground or zero (0) volts (V).  When you push the button, electrical contacts come together and connect one side of the switch to the other... this means you're connecting the pin that normally has voltage on it to zero (0) volts (V) when you press the button, which is a state the logic on the board can identify in our code later.

Soldering is a good skill to know, as it can allow not only the creation of new devices such as this, but the repair of existing devices.  A simple touch of heat and fresh solder/flux can bring a device back to life that would otherwise be headed for the landfill.  How to solder is beyond the scope of this document, but if you're completely new, I suggest looking up a few tutorials and buying a decent iron.  The absolute bottom cheapest irons are not worth the headache, you *need* a good fine tip and controllable temperature.

**Programming, or "What's that about a snake?"**

The rpi Pico/Pico2 is a great little board that runs CircuitPython... a great little language based on (you guessed it) Python.  I happen to know Python fairly well, I use it at work some and for fun some.  Now, one of the biggest benefits of Python as a language (in my opinion) is "import foo".  Meaning; chances are, whatever you want to do has been done and abstracted into a library.  So for example, if I want to read in data from a CSV file, there is a library for that, and I would load it as "import csv".

Import Foo, or Import-Fu, like software kung fu.

Anyway, this is true with this project as well.  Someone else has already done the hard part of making a gamepad/keyboard/etc HID using CircuitPython.  There are several libraries you may want to check out, depending on how you want to build your button box to behave.  I have looked into [JoystickXL](https://circuitpython-joystickxl.readthedocs.io/en/latest/) and [USB-HID](https://learn.adafruit.com/custom-hid-devices-in-circuitpython?view=all) so far, and am going with the latter because I simply need to send keystrokes.  If you want to add joysticks, touchpads, knobs, multi-position key-switches, etc etc to your device, you may find the JoystickXL lib more useful, as it supports an astonishing number of button and axis inputs.

Functionally, you must install CircuitPython to the board, then install the actual python code.  In the case of HID devices, we will need a ```boot.py``` and a ```code.py```.  In ```boot.py``` we will be sending the PC the device description and operational details.  From these details, the computer's operating system will use an appropriate driver to communicate with the device.  If it says "I'm a keyboard", Windows, Linux, or Mac OS will go "ok, you're a keyboard, I expect you to send me keystrokes per your description, and I expect to be able to control a few lights on you (capslock/numlock/scroll-lock) if you are even listening to what I send."

The code I started with is available at [github.com/adafruit/](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/CircuitPython_MacroPad_NKRO)

```boot.py``` is a bunch of bytecode stuff that is beyond the scope of this document.  There are guides and lookup tools for configuring this.  We want a keyboard, and the example is a keyboard.  copy/paste, the easiest form of programming.

```code.py``` defines the behavior of the keyboard, basically what pin is what keystroke, and if we hold or press/release the key for that pin being grounded.  Remember from the electronics section, when we push a button in this build, it connects the pin in question to electrical ground. 



**TODO: complete this document and include pictures of assembly process**

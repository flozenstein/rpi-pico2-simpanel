# rpi-pico2-simpanel
An open-source button box for simulator use.

STL files are from [TinkerCAD](https://www.tinkercad.com).  Links to Tinker This! option are including in the 3d printing section of this document.

**Introduction**

I play a lot of racing games, but also a lot of one specific game, [BeamNG.drive](https://store.steampowered.com/app/284160/BeamNGdrive/).  Less of a racing sim and more of a vehicular physics sandbox, it offers the ability to free roam large worlds in a variety of vehicles.  From a 4x4 "Go-Devil" powered Jeep type vehicle to a 400 horsepower hatchback with nitrous, the open nature of gameplay in BeamNG provides a need for many control bindings.  I found over the years that I frequently used a specific few key bindings, and that putting down a gamepad or reaching over the steering wheel to hit a keyboard key is... not as fun as mashing a button or flicking a switch. 

A friend mentioned that they had an arduino-based button box in their sim rig, and I thought "hey, I could build that, I know arduino and basic electronics".  Then I ordered the wrong arduino boards, did some research and ordered rpi-pico2 boards instead.  It might be overkill for a dozen keys worth of functionality, but it works and it works reliably without having to sort through knockoffs and bad variants of the board.  Just order your rpi pico or pico2 board from a reputable retailer like [Mouser](https://www.mouser.com/) or [Adafruit](https://www.adafruit.com/) and you'll be fine.  

Now, the case is 3d printable, or machinable out of flat stock.  I have included STL files that can be used to generate toolpaths for both methods of constructing the box.  So if you have a home manufactury machine of some variety (or have a friend who does) you should be able to make your own box.  Alternatively you could order a suitable size project box or enclosure from any number of electronics component retailers... again, Mouser or Adafruit are the first two places *I* would look.

**3d Printing or "Making a box with holes in it"**

The first part of this section will focus primarily on how to 3d print this, followed by a section on how to manufacture it with a CNC router or laser table written by my dear friend who owns such equipment.  

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

I had originally planned to build this using an Arduino or ATMEL-based microcontroller.  If you are unfamiliar with these, they are little circuit boards about the size of a stick of gum that you program over USB, and solder what I call "electronic goodies" to, and make stuff.  They can make flashy lights, set off stage effects, work as a gamepad, control a hobby robot, etc etc etc.  There is a problem, the Arduino space in hobby electronics is almost flooded with knockoff boards.  Some are good, some are meh, and some are outright bad.  But for around $5, you can have a tiny 8-bit computer that you make do nifty things.  After ordering a few, and learning upon arrival that they had "knockoff" parts on the board, I then decided to go with a somewhat newer ecosystem, the rpi pico.  From what research I did, I was able to identify that these are perfectly capable of performing HID duty, or "Human Interface Device".  Meaning they can be a gamepad or keyboard.  In the example, we'll be programming this rpi pico board to be a keyboard with 12 keys.  This then begs the question, what keys do they emulate?  Well, we're going to use keys that don't typically exist on keyboard.  At the top of your keyboard, you should have F1 through F12.  The function-keys.  Did you know most computers support F13 through F24 as well?  They're not on most keyboards, because we don't need them... but here, we can make our buttons be those unused keys and then set the control bindings in our game to respond to these new keys.  Instead of thinking of the button box as a keyboard, perhaps think of it as a keyboard extension.

Now, your rpi-pico board should be wired to switch GROUND.  Meaning you want to connect your switches and buttons between GND or electrical ground, and the IO pins.  Each switch should connect to ground and an IO pin.  You may (if you have many buttons/switches) find that a bit of perfboard works to create a ground bus.  This will permit connecting many switches to a single ground pin on the rpi pico board.

**TODO: include firmware and details about flashing board**
**TODO: complete this document and include pictures of assembly process**

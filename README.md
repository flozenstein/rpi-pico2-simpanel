# rpi-pico2-simpanel
An open-source button box for simulator use.

STL files are from TinkerCAD.  Links to Tinker This! option are including in the 3d printing section of this document.

**Introduction**

I play a lot of racing games, but also a lot of one specific game, BeamNG.drive.  Less of a racing sim and more of a vehicular physics sandbox, it offers the ability to free roam large worlds in a variety of vehicles.  From a 4x4 "Go-Devil" powered Jeep type vehicle to a 400 horsepower hatchback with nitrous, the open nature of gameplay in BeamNG provides a need for many control bindings.  I found over the years that I frequently used a specific few key bindings, and that putting down a gamepad or reaching over the steering wheel to hit a keyboard key is... not as fun as mashing a button or flicking a switch.  A friend mentioned that they had an arduino-based button box in their sim rig, and I thought "hey, I could build that, I know arduino and basic electronics".  Then I ordered the wrong arduino boards, did some research and ordered rpi-pico2 boards instead.  It might be overkill for a dozen keys worth of functionality, but it works and it works reliably without having to sort through knockoffs and bad variants of the board.  Just order your rpi pico or pico2 board from a reputable retailer like Mouser or Adafruit and you'll be fine.  Now, the case is 3d printable, or machinable out of flat stock.  I have included STL files that can be used to generate toolpaths for both methods of constructing the box.  So if you have a home manufactury machine of some variety (or have a friend who does) you should be able to make your own box.  Alternatively you could order a suitable size project box or enclosure from any number of electronics component retailers... again, Mouser or Adafruit are the first two places *I* would look.

**3d Printing or "Making a box with holes in it"**

The first part of this section will focus primarily on how to 3d print this, followed by a section on how to manufacture it with a CNC router or laser table written by my dear friend who owns such equipment.  

I have designed this to be printed easily on pretty much any FDM machine.  The box face is completely flat, and should print as the model is oriented, face-down.  This ensures a nice surface finish on the face you're going to look at most.  I recommend printing it with enough walls and top/bottom layers to make the case basically solid plastic.  This ensures that your mounting points do not become loose over time as infill begins to crack from repeated stress.

The box can be printed in PLA, ABS, PETG, weedeater line, or whatever else you feed your FDM machine.  Before committing to a 6 hour or more print to make a nice sturdy box, it's worthwhile to print the test-part first to ensure that you have the right size holes to snugly fit your switches of choice.

Test-Fit Model: 
TinkerCAD link: https://www.tinkercad.com/things/ilWKCudVXyv/edit?returnTo=%2Fdashboard&sharecode=KZdAHi8J1aMUUtoJdOfRdpk8CTP9DpqL5B3aQJiVsnA
test_fit.stl

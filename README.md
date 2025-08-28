# MiSTer_Screenshot
USB device to easily take screenshots on MiSTer

## What is it and Why Does it Exist ?

I use a Logitech K400+ keyboard/trackpad combo on my MiSTer, but it has one weakness: The
PrintScreen key is a key-combination of Windows + PrtScr, but the LogiTech's keyboard
uses another key combination for the PrtScr key, which I can never seem to remember.

So, this device is effectively a 1-keymacropad with one use: screen capture


## CircuitBoard / Parts List

This is really simple, because Adafruit sells the microcontoller board: the Adafruit
TRRS Trinkey, which is listed here, but can also be obtained from other sources such as
Digikey or Mouser:
https://www.adafruit.com/product/5954

there is also a Snap-on Enclosure for it:
https://www.adafruit.com/product/5981

For the button, I received a special "A/B Large Buttons" with an 8BitDo Retro Mechanical keyboard,
and these buttons connect with a TRS connector.  Alternately, you could use Arcade buttons in
a small enclosure and attach a simple TRS connector on a cable.


## Software

Adafruit has many useful "Learn" posts for various microcontroller boards (andother products),
and I started fromthe basis of one of their examples, which can be found here:
https://learn.adafruit.com/using-the-trrs-trinkey-as-an-assistive-technology-device

The specific code I modified is in that article, but if you just want to jump to the end and find
out how to do it easily, you will need to:
 1.  Install CircuitPython from here: https://circuitpython.org/board/adafruit_trrs_trinkey_m0/
 2.  Once that is installed, and your Trinkey shows up on your computer as a USB drvie called "CIRCUITPY",
you can install the code contained in the "src" folder in this archive.

All I really changed was to define the GPIO and key combination that is generated, so you can modify it
as you please.

Enjoy ! 

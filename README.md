# Auto Laser

This is a program to automatically note down outputs from Total Stations. I have written this program to work with a very old Leica station and a Raspberry Pi, but it should work with many other common total stations that communicate over USB and a computer.

To use, connect your computer to the station via a USB cable, and run the program. When you take a measurement with the station, it should send it down the cable to the computer, and your machine should note it down.

If something doesn't work, start an issue and I'll look into it. I can't guarantee that this will work on any other total stations, particularly newer ones, so if you have an issue with it I can't guarantee a fix, but I'll see what I can do.

Make sure you have [PySerial](https://pyserial.readthedocs.io/en/latest/index.html) installed.

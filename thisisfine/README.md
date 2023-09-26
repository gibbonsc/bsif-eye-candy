Files:
------
* boot.py : initial platform setup, run on boot. This one is stripped down; it just invokes a garbage collector once.
* main.py : the file run after the boot script. Imports necessary modules and stuff, then runs an animation in a continuous infinite loop.
* frames.py : the data containing the animation frame bitmaps, created by running a process_frames script in the frames_src subfolder
* ssd1306.py : driver library for the OLED display on the badge.

How it happened
---------------
I started with the trusty old X11 `bitmap` program,
still present in nearly every Linux desktop workstation.
The SSD1306 OLED display is 128 pixels wide and 64 pixels tall, so I used the command
`bitmap -size 128x64`
to make it present a canvas with those dimensions, then I started drawing:


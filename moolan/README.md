I made a ["Moon Lander" game](https://en.wikipedia.org/wiki/Lunar_Lander_%28video_game_genre%29)
for the BSides Idaho Falls 2024 electronic badge.

Files:
------
- boot.py : Initial platform setup, run on boot. (This one is empty.)
- main.py : Executed after the boot script. THis one imports modules and stuff, then runs the moon lander simulation.
- ssd1306.py : driver library for the OLED display on the badge.
- i2c_eeprom.py : required for OLED display driver.
- moolan_pyg.py : For convenience, I first coded the game with this code,
which uses [pygame](https://www.pygame.org/) and CPython.
Getting it was working well enough on my PC made it easier to adapt it to the MicroPython version found in main.py.

Install:
--------
The [rshell](https://github.com/dhylands/rshell)
module has become my favorite way to transfer files between my computer and the badge.
I just type `rsync . /pyboard` or `rsync /pyboard .` to transfer files to or from the badge, respectively.
Then I type `repl` to get a prompt on the badge, and [CTRL]+[D] to reboot the badge to run its new code.

How to play it:
---------------------------------------
Just use the "D-PAD" buttons at the left of the badge:
- UP : start the game
- DOWN : fire the retro-thruster rocket, to slow the spacecraft's descent.
- LEFT : fire the left rocket, to make the spacecraft drift more to the right.
- RIGHT : fir the right rocket, to make the spacecraft drift more to the left.

You can also push either of the two buttons beneath the display to abort the game and start over.

Try to manoever the spacecraft to touch down on the landing pad at the bottom of the display screen,
but be careful.
Its vertical velocity must be less than 2 to land safely.
If it touches down too fast, or if it misses the landng pad, it will crash instead!
The top right corner of the display shows your craft's vertical and horizontal velocities.

The NeoPixel LEDs will turn red when you crash, white when you abort, or green when you land successfully.
Then you can press UP to try again!

Credits: some early proposals for the BSides Idaho Falls 2025 logo included images of the moon,
which inspired this little project.
It also gave me a reason to keep practicing my Python skills,
so that I had something new to show to my "Intro to Programming" and "Programming with Functions" students.
Thanks, students! You're awesome!

Also, much obliged to Spectr03, Riley, YodaMaster, Hannah, meecles, roman_fire, Xanadu2600, YaKcm, Ginger, etc.

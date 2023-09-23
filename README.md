Files:
-------
 * load_memories.py : Preparation script to flash memory contents. requires `funcs.py` on the device
 * main.py          : actual main file. requires pretty much everything else.
 * boot.py          : initial platform setup, run on boot. you probably don't
                      need to mess with this, though it imports all of the stuff from funcs.py (as
                      fu.\*) which only works for main, not other files (at least, not other files
                      run through the [raw] REPL)). 
 * secrets.py       : file with the wifi SSID/password
 * i2c\_eeprom.py, ssd1306.py : specific driver libraries
 * firmware/.*      : The actual UF2 image for the pico w. Load this if it is showing up like a usb drive
                      called `RPI RP2` or similar (copy to drive and sync/unmount).

Running/Loading code
--------------------
Most of the development work has been done using Adafruit's Ampy tool (not really supported by
adafruit at this point, as they've switched to circuitpython). To install, run `pip install
adafruit-ampy`, as you want this tool not the image-processing for active matter experiments tool.
And probably you want to throw this in its own little venv as a good practice and to avoid
accidentally screwing up system/user python stuff (it happens. it really does.)

You can also use any other micropython-specific tool to load code (`mpremote, etc`). The following
assumes that you are using ampy.

To load a file, run `ampy -p <serial_port> load <file>`. This overwrites with no confirmation :)
To see what is on the board, run `ampy -p <serial_port> ls`.
To run a file, run `ampy -p <serial_port> run <file>`. This will run the file in the foreground,
piping all output to the terminal until the program exits. If the program infinitely loops, add
`-n/--no-output` to get it to not wait to return.

Have fun!

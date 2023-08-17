import machine
import ssd1306
import time
import bad_funcs as bf
import eye_candy as ec

# Init & frash neopixels
# BS Idaho Falls 2021 badge: two pixels, pin zero
np = bf.init_neopix(machine.Pin(0),2)
bf.frash(np)

# Init the SSD1306 display
display = ec.init_display()

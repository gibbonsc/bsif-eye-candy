import ssd1306
import time
import machine
import neopixel

def init_neopix(pin_num, pixel_count):
    np = neopixel.NeoPixel(pin_num, pixel_count)
    return np

def neo_test(np):
    np[0] = (25, 0, 0) # set to red, full brightness
    np[1] = (0, 25, 0) # set to green, full brightness
    np.write()

def shine(np):
    n = np.n
    for i in range(n):
        np[i] = (25, 25, 25)
    np.write()
    time.sleep_ms(500)
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

def neo_attr(np):
    for i in range(25):
        np[0] = (i,i,0) # yeller
        np[1] = (i,0,i) # magenta
        np.write()
        time.sleep_ms(50)
    for i in range(25):
        np[0] = (24-i,24-i,0) # yeller
        np[1] = (24-i,0,24-i) # magenta
        np.write()
        time.sleep_ms(50)

def frash(np):
    n = np.n
    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(40)
    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()




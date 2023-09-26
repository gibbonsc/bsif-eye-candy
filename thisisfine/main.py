import ssd1306
import framebuf
import machine
import frames
import time

frms=frames.init_frames()
i2c0=machine.I2C(0,scl=machine.Pin(5),sda=machine.Pin(4),freq=400000)
d=ssd1306.SSD1306_I2C(128,64,i2c0,0x3c)
delay=1/6

while True:
    for i in range(0,3):
        time.sleep(delay)
        fbuf=framebuf.FrameBuffer(frms[i],128,64,framebuf.MONO_HMSB)
        d.fill(0)
        d.blit(fbuf,0,0,0)
        d.text('This is fine',32,0)
        d.show()


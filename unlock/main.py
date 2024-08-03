import ssd1306
import framebuf
import machine
import frames
import time

frms=frames.init_frames()
fseq=[0,1,2,3,4,5,5,5,5,5]
i2c0=machine.I2C(0,scl=machine.Pin(5),sda=machine.Pin(4),freq=400000)
d=ssd1306.SSD1306_I2C(128,64,i2c0,0x3c)
delay=1/6

while True:
    for i in fseq:
        time.sleep(delay)
        fbuf=framebuf.FrameBuffer(frms[i],48,48,framebuf.MONO_HMSB)
        d.fill(0)
        d.blit(fbuf,0,16,0)
        if i==5:
            d.text('Unlocked!',32,0)
        d.show()


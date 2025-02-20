import ssd1306,framebuf,array
from machine import Pin,I2C
from neopixel import NeoPixel
from random import randint
import time

button1=Pin(1,Pin.IN,Pin.PULL_UP)
button0=Pin(0,Pin.IN,Pin.PULL_UP)
buttonD=Pin(7,Pin.IN,Pin.PULL_UP)
buttonL=Pin(8,Pin.IN,Pin.PULL_UP)
buttonR=Pin(9,Pin.IN,Pin.PULL_UP)
buttonU=Pin(10,Pin.IN,Pin.PULL_UP)
np_pin = Pin(6)
np = NeoPixel(np_pin,3)
np[0]=np[1]= np[2]=(0,0,0)
np.write()
i2c0=I2C(0,scl=Pin(5),sda=Pin(4),freq=400000)
d=ssd1306.SSD1306_I2C(128,64,i2c0,0x3c)

delay=1.0/3.0
crash=win=quitting=playing=False
y_vel=x_vel=0.0
banner='UP to start'
sprite_id=1
cx=59.0;cy=0.0;tx=58;ty=62
jets=[False,False,False]

def render_pf():
    craft_v = array.array('B',[0,10, 2,8, 3,0, 9,0, 10,8, 12,10, 10,10, 8,7, 4,7, 2,10])
    crash_v = array.array('B',[0,5, 3,0, 4,6, 7,0, 6,6, 10,2, 8,7, 12,8, 6,9, 2,7])
    fbuf=framebuf.FrameBuffer(bytearray(16*64*1),128,64,framebuf.MONO_HMSB)
    fbuf.fill(0)
    if sprite_id==0:
        svg=crash_v
    else:
        svg=craft_v
    ix=int(cx); iy=int(cy)
    fbuf.poly(ix,iy,svg,1)
    if jets[0]:
        fbuf.vline(ix+6,iy+10,3,1)
    if jets[1]:
        fbuf.hline(ix-3,iy+5,3,1)
    if jets[2]:
        fbuf.hline(ix+13,iy+5,3,1)
    fbuf.rect(tx,ty,15,2,1)
    d.fill(0)
    d.blit(fbuf,0,0,0)
    # HUD
    d.text(banner,8,24)
    d.text('V:%2d'%(-y_vel),128-32,6)
    d.text('H:%2d'%(x_vel),128-32,14)
    d.show()

def attract():
    global playing
    # @@@ add neopixel blinkies?
    if crash:
        np[0]=np[1]=np[2]=(15,0,0)
    elif win:
        np[0]=np[1]=np[2]=(0,15,0)
    else:
        np[0]=np[1]=np[2]=(15,15,15)
    np.write()
    while not playing:
        if crash:
            sprite_id=0
        else:
            sprite_id=1
        render_pf()
        time.sleep(delay)
        if buttonU.value()==0:
            print('U: leaving attract')
            playing=True
    np[0]=np[1]= np[2]=(0,0,0)
    np.write()

def play():
    global playing,y_vel,x_vel,cx,cy,sprite_id,banner,jets,crash,win
    print('starting play')
    while playing:
        time.sleep(delay)
        if button1.value()==0 or button0.value()==0:
            print('1/0: forfeit')
            playing=False
        if buttonD.value()==0:
            print('D: down')
            y_vel -= 1.0 + 0.388326
            jets[0]=True
        if buttonL.value()==0:
            print('L: left')
            x_vel += 1.0
            jets[1]=True
        if buttonR.value()==0:
            print('R: right')
            x_vel -= 1.0
            jets[2]=True

        y_vel += 0.388326
        cy += y_vel; cx += x_vel
        if cy > 53:
            if y_vel >= 2.0:
                crash=True; playing=False
            elif tx-5 <= int(cx) <= tx+5:
                win=True; playing=False
            else:
                crash=True; playing=False
        sprite_id=1
        if win:
            banner='WINNER!'
        elif crash:
            banner='CRASHED'
            sprite_id=0
        elif not playing:
            banner='(forfeit)'
        else:
            banner=''
        render_pf()
        jets=[False,False,False]
    print('leaving play')

render_pf()

while not quitting:
    attract()
    if not quitting:
        cx=float(randint(2, 128-15)); cy=0
        tx=randint(64-48,64+48); ty=62
        y_vel=x_vel=0.0
        crash=win=False
        play()


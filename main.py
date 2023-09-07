import machine
import ssd1306
import time
import bad_funcs as bf
import eye_candy as ec
import frames as fr

delay = 1.0 / 12    # 12 FPS animation rate
frame = 6
# Init & frash neopixels for badge
# BF Idaho Falls 2021 badge: two pixels, pin zero
np = bf.init_neopix(machine.Pin(0),2)
bf.frash(np)

# Init the display for our use...
display = ec.init_display()
frames = fr.init_frames()
seqs = ec.init_seqs()

frame_num = len(seqs['winks']) - 1

#exit()

while True:

    ec.show_frame(display, frames, seqs, 'winks', frame_num)
    frame_num = (frame_num - 1) % len(seqs['winks'])
    time.sleep(delay)

    #bf.shine(np)
    #ec.bstp32_blit(display)
    #time.sleep(delay)

    #ec.state_map_blit(display)
    #bf.neo_attr(np)
    #time.sleep(delay)

    #ec.all_ascii_backward(display)
    #time.sleep(delay)

    #ec.rect_nest_dolls(display)
    #time.sleep(delay)

    #ec.state_map_slow(display)
    #bf.frash(np)
    #time.sleep(delay)

    #ec.st_andrew_cross(display)
    #time.sleep(delay)

    #ec.ebegs_blit(display)
    #time.sleep(delay)

    #ec.mp_logo(display)
    #bf.neo_test(np)
    #time.sleep(delay)


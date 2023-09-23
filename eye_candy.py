#import machine # already imported in funcs.py
#import ssd1306
#import time
#import framebuf #already imported in ssd1306.py

def init_display():
    sda = machine.Pin(4)
    scl = machine.Pin(5)
    i2c = machine.I2C(scl=scl, sda=sda, freq=400000)
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.fill(1)
    display.show()
    time.sleep(0.14)
    display.fill(0)
    display.show()
    return display

def init_seqs():
    render_seq_dict={}
    render_seq_dict['winks']=[0,0,0,0,1,2,2,1,0,0,3,4,4,3,0,0,5,6,6,5,0,0,0]
    render_seq_dict['winks'].reverse()
    return render_seq_dict

def init_anims(display,frame_list,render_seq_dict):
    tach=""
    for file in ['p1', 'pq11', 'pq12', 'pq31', 'pq32', 'pq41', 'pq42']:
        with open(file+'.xbm') as fh:
            fh.readline()
            fh.readline()
            fh.readline()
            ba=[]
            while True:
                line = fh.readline().strip().strip(",").strip("};")
                if not line:
                    break
                octets = line.split(", ")
                for octet in octets:
                    ba.append(int(octet,0))
            frame_list.append(bytearray(ba))
            tach = tach + "."
            display.text(tach, 40, 0, 1)
            display.show()
    
    render_seq_dict['winks'] = [0,0,0,0,1,2,2,1,0,0,3,4,4,3,0,0,5,6,6,5,0,0,0]
    render_seq_dict['winks'].reverse()

def show_frame(display, frame_list, render_seq_dict, anim_id, frame_index):
    # 64 rows, 128 pixels per row, 1 bit per monochrome-color
    cur_index = render_seq_dict[anim_id][frame_index]
    cur_buffer = frame_list[cur_index]
    fbuf = framebuf.FrameBuffer(cur_buffer, 128, 64, framebuf.MONO_HMSB)
    display.fill(0)
    display.blit(fbuf,0,0,0)
    display.show()

def bou(display,fram):
    display.fill(0)
    display.fill_rect(fram*8,fram*8,7,7,1)
    display.show()

# MicroPython logo demo code, from
# https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html#ssd1306
def mp_logo(display):
    display.fill(0) # clear pixels prior to rendering new pixels
    display.fill_rect(0, 0, 32, 32, 1)
    display.fill_rect(2, 2, 28, 28, 0)
    display.vline(9, 8, 22, 1)
    display.vline(16, 2, 22, 1)
    display.vline(23, 8, 22, 1)
    display.fill_rect(26, 24, 2, 4, 1)
    display.text('MicroPython', 40, 0, 1)
    display.text('SSD1306', 40, 12, 1)
    display.text('OLED 128x64', 40, 24, 1)
    display.show()

def all_ascii_backward(display):
    display.fill(0)
    for row in range(8):
        str16 = ''
        for col in range(16):
            str16 += chr(127 - (16 * row + col))
        display.text(str16, 0, row * 8, 1)
    display.show()

def st_andrew_cross(display):
    display.fill(0)
    display.line(0,0,127,63,1)
    display.line(0,63,127,0,1)
    display.show()

def rect_nest_dolls(display):
    display.fill(1)
    for row in range(10):
        col = row
        left = 1 + 3 * col
        top = 1 + 3 * row
        width = 126 - 6 * col
        height = 62 - 6 * row
        display.rect(left, top, width, height, 0)
    display.show()

def state_map_slow(display):
    display.fill(0)
    # 64 rows, 40 pixels per row, 1 bit per monocrhome-color
    blit_buf = bytearray(64 * 40//8 * 1)
    fbuf = framebuf.FrameBuffer(blit_buf, 40, 64, framebuf.MONO_VLSB)

    # slowly trace map outline
    dot2dot = [2,62, 2,46, 3,44, 1,43, 1,40, 5,32, 5,31, 3,29, 3,28, 2,1, 8,1, 8,3, 9,11, 10,15, 16,22, 18,23, 17,25, 17,32, 20,31, 23,38, 24,38, 26,42, 35,39, 37,41, 37,62, 2,62]
    (x_pt,y_pt) = (dot2dot[0], dot2dot[1])
    for i in range(2, len(dot2dot), 2):
        (x_tg,y_tg) = (dot2dot[i], dot2dot[i+1])
        fbuf.line(x_pt, y_pt, x_tg, y_tg, 1)
        display.blit(fbuf,128-40,0,0)
        display.show()
        time.sleep(0.1)
        (x_pt,y_pt) = (x_tg,y_tg)

    # highlight Idaho Falls on the map
    fbuf.line(30,48,32,48,1)
    fbuf.line(31,47,31,49,1)

    # display.blit(fbuf,0,0,0)
    display.blit(fbuf,128-40,0,0)
    display.show()
    #print(blit_buf)

def state_map_blit(display):
    # rapid block-image-transfer (BLIT)
    # 64 rows, 40 pixels per row, 1 bit per monocrhome-color
    blit_buf = bytearray(b'\x00\x00\xfe\x02\x02\x02\x02\x02~\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x01\x02\x0c\x10 @\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x0c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x06\x18`@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x0f\xc80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x06\x04\x02\x02\x02\x81\x01\x01\x00\x00\x01\xfe\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x01\x00\x00\x00\x00\xff\x00\x00\x00\x00\x7f@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\x7f\x00\x00')
    fbuf = framebuf.FrameBuffer(blit_buf, 40, 64, framebuf.MONO_VLSB)
    display.fill(0)
    display.blit(fbuf,128-40,0,0)
    display.show()

def bsanimateframe(display,anim_id,anim_frame):
    # 64 rows, 128 pixels per row, 1 bit per monochrome-color
    potato_buf = bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x1f\xfc\xff\xf0\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc3\xff\xff\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf8\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff?\xfe\xff\xff\xff\xe3\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x8f\xff\xff\xff\xff\x9f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\xff\xff\xff\xff?\xfe\xff\xff\xff\xff\xff\xff\xff\x07\x00\xfe\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\x01\xf0\xff\xff\xff?\xfe\xff\xff\xf9\xff\xff\xff\xff\xff\x0f\xfc\xff\xff\xff\xff\x83\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xe1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xcf\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xff\x7f\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\x9f\xff\xff\xff\xff?\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbf\xff\xff\xff\xff\xbf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x7f\xff\xff\xff\xff\x9f\xff\xff\xff\xff\xff\xff\xff\x0f\xf8\xff\xff\xfe\xff\xff\xff\xdf\xff\xff\xff\xff\xff\xff\xff\xf1\xc7\xff\xff\xfd\xff\xff\xff\xdf\xff\xff\xff\xff\xff\xff\xff\xfd\x9f\xff\xff\xfb\xff\xff\xff\xef\xff\xff\x03\xf8\xff\xff\xff}<\xff\xff\xf3\xff\xff\xff\xef\xff?\xfe\xe3\xff\xff\xff}|\xff\xff\xf7\xff\xff\xff\xef\xff\x8f\xff\xcf\xff\xff\xffy\xfc\xfe\xff\xef\xff\xff\xff\xe7\xff\xcf\x1f\xbf\xff\xff\xff\xf3\xff\xfe\xff\xef\xff\xff\xff\xf7\xff\xdf\x1f\x7f\xff\xff\xff\xe7?\xfe\xff\xcf\xff\xff\xff\xf7\xff\x1f\x1f?\xff\xff\xff\x0f\x00\xff\xff\xdf\xff\xff\xff\xf7\xff\x7f\xfe\x0f\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xf7\xff\xff\xc1\xe7\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xf7\xff\xff\x1f\xf8\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdf\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xcf\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xef\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc1\xff\xef\xff\xff\xff\xe7\xff\xff\xff\xff\xff\xff\xff\xff?\xfe\xff\xef\xff\xff\xff\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf7\xff\xff\xff\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf3\xff\xff\xff\xcf\xff\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xf9\xff\xff\xff\xdf\xff\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\x9f\xff\xf1\xff\xff\xff\x8f\xff\xff\xff\xff\x7f\xfe\xff\xff\xff\xbf\xff\xff\xff\xff\xff?\xfe\xff\xff\xff?\xff\xff\xff\xff?\xff\xff\xff\xff\xff\xff\xe1\xff\xff\xff\xcf\xff\xff\xff\xff\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe7\xff\xff\xff\xff\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf9\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xff\xff?\xfc\xff\xff\xff\xff\xff\xf9\xff\xff\xff\xff\xff\xff\xff\xff\x87\xff\xff\xff\xff\xff\xff\xf3\xff\xff\xff\xff\xff\xff\xff\xff\xf1\xff\xff\xff\xff\xff\xff\xcf\xff\xff\xff\xff\xff\xff\xff\x7f\xfc\xff\xff\xff\xff\xff\xff\x9f\xff\xff\x01\xf8\xff\xff\xff\x0f\xff\xff\xff\xff\xff\xff\xff\x7f\xfe\x0f\xfc\x03\xff\xff\xff\xe1\xff\xff\xff\xff\xff\xff\xff\xff\x00\xf0\xff\x7f\xf8\xff\x1f\xfc\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf3\xff\xc0\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x0f\x00\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
    fbuf = framebuf.FrameBuffer(potato_buf, 128, 64, framebuf.MONO_HMSB)
    display.blit(fbuf,0,0,0)
    display.show()

def bstp32_blit(display):
    # 32 rows, 32 pixels per row, 1 bit per monocrhome-color
    blit_buf = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xe0\xf8\xfc\xfc\xfe\x7f\x3f\x1f\x1f\x1f\x1f\x1f\x3f\x7f\xfe\xfc\xfc\xf8\xe0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xff\xff\xff\xff\xff\xe0\xc0\x80\x0e\x1f\x1f\x1f\x0e\x00\x00\x00\x1f\x1f\x1f\x3f\x3f\xfc\xfc\xfc\xfc\xfc\x00\x00\x00\x70\xf8\xf8\xf8\x70\x01\x03\x07\xff\xff\xff\xff\xfe\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x07\x1f\x3f\x3f\x7f\xfe\xfc\xf8\xf8\xf8\xf8\xf8\xfc\xfe\x7f\x3f\x3f\x1f\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    fbuf = framebuf.FrameBuffer(blit_buf, 32, 32, framebuf.MONO_VLSB)
    display.fill(0)
    display.blit(fbuf,0,32,0)
    display.blit(fbuf,96,0,0)
    display.show()

def bit_patterns_blit(display):
    # 32 rows, 32 pixels per row
    blit_buf = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xe0\xf8\xfc\xfc\xfe\x7f\x3f\x1f\x1f\x1f\x1f\x1f\x3f\x7f\xfe\xfc\xfc\xf8\xe0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xff\xff\xff\xff\xff\xe0\xc0\x80\x0e\x1f\x1f\x1f\x0e\x00\x00\x00\x1f\x1f\x1f\x3f\x3f\xfc\xfc\xfc\xfc\xfc\x00\x00\x00\x70\xf8\xf8\xf8\x70\x01\x03\x07\xff\xff\xff\xff\xfe\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x07\x1f\x3f\x3f\x7f\xfe\xfc\xf8\xf8\xf8\xf8\xf8\xfc\xfe\x7f\x3f\x3f\x1f\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    fbuf = framebuf.FrameBuffer(blit_buf, 32, 32, framebuf.MONO_VLSB)
    display.fill(0)
    display.blit(fbuf,0,32,0)
    display.blit(fbuf,96,0,0)
    display.show()

def ebegs_blit(display):
    # 16 rows, 8 pixels per row
    blit_buf = bytearray(b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff')
    fbuf = framebuf.FrameBuffer(blit_buf, 8, 16, framebuf.MONO_HLSB)
    display.fill(0)
    display.blit(fbuf,0,16,0)
    display.blit(fbuf,32,0,0)
    display.blit(fbuf,40,40,0)
    display.show()



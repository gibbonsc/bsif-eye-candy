#import funcs as fu # This is redundant... and just takes up extra memory as it is in boot.py

# # I2C Blob to write:
# f = open("supersecret_1.txt", "r")
# iblob = f.read()
iblob = b'testing_txt_data'

# # SPI Blob to write:
# f = open("supersecret_2.txt", "r")
# sblob = f.read()
sblob = '''def do_stuff("ptr_str"):
    print(atr_str)
    return 0

def do_smore("ptr_str"):
    print(btr_str)
    return 0

def do_more("ptr_str"):
    print(ctr_str)
    return 0
'''

# Initialize our neopixel(s)
np = fu.init_neo()
fu.test_neo_1(np)
# Setup a loop counter for controlling our tasks
# Plan to potentially convert this to "utime" to use the internal clock
loop_ctr = 0
prime_ctr = 0
# Initialize our I2C/OLED/SPI devices
i2c_h = fu.init_i2c()
oled_handle = fu.init_oled(i2c_h)
spi_hnd, scs = fu.init_spi_eeprom()

# Initialize our display with a default menu...
fu.oled_update(oled_handle)

fu.write_i2c(i2c_h, iblob)
fu.time.sleep(.01)
read_data = fu.read_i2c(i2c_h)
print("i2c_data: ", read_data)

fu.spi_write(spi_hnd, scs, 0, sblob)
read_data = fu.spi_read(spi_hnd, scs, 0, 300)
print("spi_data: ", read_data)
tmp = str(read_data)
print("spi_data_str: ", tmp)
eval(tmp)
do_stuff('something_to_print')

fu.oled_update(oled_handle)
fu.test_neo_3(np)
fu.time.sleep(1)
fu.oled_test_write(oled_handle)
fu.test_neo_1(np)
fu.time.sleep(1)
print("Flash Done")

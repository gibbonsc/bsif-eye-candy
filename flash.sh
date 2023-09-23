#!/usr/bin/bash -x

MY_AMPY=/home/cgibbons/venv/bin/ampy
#while :
#do
    if [ -d '/home/cgibbons/Study/bsside/this_should_not_exist' ]
    then
        echo "Found Dir... starting flash"
        sleep 2
        # cp firmware/rp2-pico-w-20230426-v1.20.0.uf2 /media/spectre03/RPI-RP2/
        #cp firmware/micropython-firmware-pico-w-130623.uf2 /media/spectre03/RPI-RP2/
        sleep 3
        # $MY_AMPY -p /dev/ttyACM0 rm main.py
        # $MY_AMPY -p /dev/ttyACM0 put boot.py
        # $MY_AMPY -p /dev/ttyACM0 put funcs.py
        # $MY_AMPY -p /dev/ttyACM0 put ssd1306.py
        # $MY_AMPY -p /dev/ttyACM0 put secrets.py
        # $MY_AMPY -p /dev/ttyACM0 put i2c_eeprom.py
        # python3 -c "print('\x04')" > /dev/ttyACM0
        # $MY_AMPY -p /dev/ttyACM0 run load_memories.py
        # $MY_AMPY -p /dev/ttyACM0 put main.py
        # echo "Test Complete... disconnect!"
        sleep 1
        exec $0
    elif [[ -e /dev/ttyACM0 ]];
    then
        echo "Found ttyACM0... starting flash"
        $MY_AMPY -p /dev/ttyACM0 rm boot.py
        $MY_AMPY -p /dev/ttyACM0 rm funcs.py
        $MY_AMPY -p /dev/ttyACM0 rm ssd1306.py
        $MY_AMPY -p /dev/ttyACM0 rm main.py
        $MY_AMPY -p /dev/ttyACM0 rm secrets.py
        $MY_AMPY -p /dev/ttyACM0 rm i2c_eeprom.py
        $MY_AMPY -p /dev/ttyACM0 put boot.py
        $MY_AMPY -p /dev/ttyACM0 put funcs.py
        $MY_AMPY -p /dev/ttyACM0 put ssd1306.py
        $MY_AMPY -p /dev/ttyACM0 put secrets.py
        $MY_AMPY -p /dev/ttyACM0 put i2c_eeprom.py
        $MY_AMPY -p /dev/ttyACM0 put main.py
        sleep 1
        /home/cgibbons/venv/bin/python3 -c "print('\x04')" > /dev/ttyACM0
        sleep 1
        $MY_AMPY -p /dev/ttyACM0 reset
        # sleep 25
        echo "Prog Complete... reconnect!"
        sleep 9
        $MY_AMPY -p /dev/ttyACM0 run load_memories.py
        sleep 1
        echo "Test Complete... disconnect!"
        sleep 10
        #exec $0
    else
        # echo "sleeping 1"
        sleep 1
    fi
#done

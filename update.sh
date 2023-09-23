#!/usr/bin/bash
while :
do
    if [[ -e /dev/ttyACM0 ]];
    then
        echo "Found ttyACM0... starting flash"
        # ampy -p /dev/ttyACM0 rm boot.py
        # ampy -p /dev/ttyACM0 rm funcs.py
        # ampy -p /dev/ttyACM0 rm ssd1306.py
        # ampy -p /dev/ttyACM0 rm main.py
        # ampy -p /dev/ttyACM0 rm i2c_eeprom.py
        ampy -p /dev/ttyACM0 rm secrets.py
        # ampy -p /dev/ttyACM0 put boot.py
        # ampy -p /dev/ttyACM0 put funcs.py
        # ampy -p /dev/ttyACM0 put ssd1306.py
        # ampy -p /dev/ttyACM0 put main.py
        # ampy -p /dev/ttyACM0 put i2c_eeprom.py
        ampy -p /dev/ttyACM0 put secrets.py
        python3 -c "print('\x04')" > /dev/ttyACM0
        ampy -p /dev/ttyACM0 run test.py
        echo "Test Complete... disconnect!"
        sleep 15
        exec $0
    else
        # echo "sleeping 1"
        sleep 1
    fi
done

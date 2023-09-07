#!/bin/bash
MY_AMPY=/home/cgibbons/venv/bin/ampy

python3 ./frames_src/process_frames.py > frames.py

for f in `ls -1 *.py`
do
    echo "Uploading: $f"
    $MY_AMPY -p /dev/ttyUSB0 -b 115200 put $f
done
$MY_AMPY -p /dev/ttyUSB0 -b 115200 ls


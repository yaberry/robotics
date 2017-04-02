#!/bin/bash 

raspistill --nopreview -w 640 -h 480 -q 5 -o /home/pi/ybot/stream/pic.jpg -tl 500 -t 9999999 &

LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /home/pi/ybot/stream -n pic.jpg" -o "output_http.so -w /home/pi/code/mjpg-streamer/www/" &


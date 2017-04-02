#!/bin/bash 

pid=`ps -edf | grep "raspistill" | grep -v "grep" |  awk '{print $2}'`

echo "killing $pid"

kill -9  "$pid"


pid=`ps -edf | grep "mjpg-streamer" | grep -v "grep" |  awk '{print $2}'`

echo "killing $pid"

kill -9  "$pid"


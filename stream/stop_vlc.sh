#!/bin/bash 


pid=`ps -edf | grep "raspivid" | grep -v "grep" |  awk '{print $2}'`

echo "killing $pid"

kill -9  "$pid"


pid=`ps -edf | grep "cvlc" | grep -v "grep" |  awk '{print $2}'`

echo "killing $pid"

kill -9  "$pid"





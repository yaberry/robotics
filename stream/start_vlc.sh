#!/bin/bash 

/opt/vc/bin/raspivid -o - -t 0 -hf -w 1024 -h 768 -fps 20|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264 &


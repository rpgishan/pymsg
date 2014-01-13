#!/bin/sh
stdbuf -oL python ../../activemq/src/test_send.py 1024 &> ../../activemq/results/1024/5_5producer1.txt &
stdbuf -oL python ../../activemq/src/test_send.py 1024 &> ../../activemq/results/1024/5_5producer2.txt &
stdbuf -oL python ../../activemq/src/test_send.py 1024 &> ../../activemq/results/1024/5_5producer3.txt &
stdbuf -oL python ../../activemq/src/test_send.py 1024 &> ../../activemq/results/1024/5_5producer4.txt &
stdbuf -oL python ../../activemq/src/test_send.py 1024 &> ../../activemq/results/1024/5_5producer5.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py &> ../../activemq/results/1024/5_5consumer6.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py &> ../../activemq/results/1024/5_5consumer7.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py &> ../../activemq/results/1024/5_5consumer8.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py &> ../../activemq/results/1024/5_5consumer9.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py &> ../../activemq/results/1024/5_5consumer10.txt &

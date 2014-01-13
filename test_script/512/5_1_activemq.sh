#!/bin/sh
stdbuf -oL python ../../activemq/src/test_send.py 512 &> ../../activemq/results/512/5_1producer1.txt &
stdbuf -oL python ../../activemq/src/test_send.py 512 &> ../../activemq/results/512/5_1producer2.txt &
stdbuf -oL python ../../activemq/src/test_send.py 512 &> ../../activemq/results/512/5_1producer3.txt &
stdbuf -oL python ../../activemq/src/test_send.py 512 &> ../../activemq/results/512/5_1producer4.txt &
stdbuf -oL python ../../activemq/src/test_send.py 512 &> ../../activemq/results/512/5_1producer5.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py &> ../../activemq/results/512/5_1consumer.txt &

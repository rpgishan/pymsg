#!/bin/sh
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer1.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer2.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer3.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer4.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer5.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer6.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer7.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer8.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer9.txt &
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/10_1producer10.txt &
stdbuf -oL python ../activemq/src/test_receive_async.py &> ../activemq/results/10_1consumer.txt &

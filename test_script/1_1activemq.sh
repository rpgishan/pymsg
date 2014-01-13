#!/bin/sh
stdbuf -oL python ../activemq/src/test_send.py &> ../activemq/results/1_1producer.txt &
stdbuf -oL python ../activemq/src/test_receive_async.py &> ../activemq/results/1_1consumer.txt &

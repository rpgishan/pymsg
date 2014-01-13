#!/bin/sh
stdbuf -oL python ../zeromq/src/test_send.py &> ../zeromq/results/1_1producer.txt &
stdbuf -oL python ../zeromq/src/test_receive_async.py &> ../zeromq/results/1_1consumer.txt &

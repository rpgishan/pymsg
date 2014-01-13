#!/bin/sh
stdbuf -oL python ../../zeromq/src/test_send.py &> ../../zeromq/results/256/5_1producer1.txt &
stdbuf -oL python ../../zeromq/src/test_send.py &> ../../zeromq/results/256/5_1producer2.txt &
stdbuf -oL python ../../zeromq/src/test_send.py &> ../../zeromq/results/256/5_1producer3.txt &
stdbuf -oL python ../../zeromq/src/test_send.py &> ../../zeromq/results/256/5_1producer4.txt &
stdbuf -oL python ../../zeromq/src/test_send.py &> ../../zeromq/results/256/5_1producer5.txt &
stdbuf -oL python ../../zeromq/src/test_receive_async.py &> ../../zeromq/results/256/5_1consumer.txt &

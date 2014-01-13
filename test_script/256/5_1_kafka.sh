#!/bin/sh
stdbuf -oL python ../../kafka/src/test_send.py &> ../../kafka/results/256/5_1producer1.txt &
stdbuf -oL python ../../kafka/src/test_send.py &> ../../kafka/results/256/5_1producer2.txt &
stdbuf -oL python ../../kafka/src/test_send.py &> ../../kafka/results/256/5_1producer3.txt &
stdbuf -oL python ../../kafka/src/test_send.py &> ../../kafka/results/256/5_1producer4.txt &
stdbuf -oL python ../../kafka/src/test_send.py &> ../../kafka/results/256/5_1producer5.txt &
stdbuf -oL python ../../kafka/src/test_receive_sync.py &> ../../kafka/results/256/5_1consumer.txt &

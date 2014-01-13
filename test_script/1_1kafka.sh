#!/bin/sh
stdbuf -oL python ../kafka/src/test_send.py &> ../kafka/results/1_1producer.txt &
stdbuf -oL python ../kafka/src/test_receive_async.py &> ../kafka/results/1_1consumer.txt &

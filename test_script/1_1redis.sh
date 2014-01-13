#!/bin/sh
stdbuf -oL python ../redis/src/test_send.py &> ../redis/results/1_1producer.txt &
stdbuf -oL python ../redis/src/test_receive_async.py &> ../redis/results/1_1consumer.txt &

#!/bin/sh
stdbuf -oL python ../../kafka/src/test_send.py 1024 &> ../../kafka/results/1024/1_1producer.txt &
stdbuf -oL python ../../kafka/src/test_receive_sync.py 1024 &> ../../kafka/results/1024/1_1consumer.txt &

#!/bin/sh
stdbuf -oL python ../../kafka/src/test_send.py 256 &> ../../kafka/results/256/1_1producer.txt &
stdbuf -oL python ../../kafka/src/test_receive_sync.py 256 &> ../../kafka/results/256/1_1consumer.txt &

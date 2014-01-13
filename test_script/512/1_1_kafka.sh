#!/bin/sh
stdbuf -oL python ../../kafka/src/test_send.py 512 &> ../../kafka/results/512/1_1producer.txt &
stdbuf -oL python ../../kafka/src/test_receive_async.py 512 &> ../../kafka/results/512/1_1consumer.txt &

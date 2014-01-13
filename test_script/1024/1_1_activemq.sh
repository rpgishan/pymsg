#!/bin/sh
stdbuf -oL python ../../activemq/src/test_send.py 1024 &> ../../activemq/results/1024/1_1producer.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py 1024 &> ../../activemq/results/1024/1_1consumer.txt &

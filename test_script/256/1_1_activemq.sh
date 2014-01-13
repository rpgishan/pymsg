#!/bin/sh
stdbuf -oL python ../../activemq/src/test_send.py 256 &> ../../activemq/results/256/1_1producer.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py 256 &> ../../activemq/results/256/1_1consumer.txt &

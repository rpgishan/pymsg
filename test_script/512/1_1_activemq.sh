#!/bin/sh
stdbuf -oL python ../../activemq/src/test_send.py 512 &> ../../activemq/results/512/1_1producer.txt &
stdbuf -oL python ../../activemq/src/test_receive_sync.py 512 &> ../../activemq/results/512/1_1consumer.txt &

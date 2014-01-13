#!/bin/sh
stdbuf -oL python ../rabbitmq/src/test_send.py &> ../rabbitmq/results/1_1producer.txt &
stdbuf -oL python ../rabbitmq/src/test_receive_async.py &> ../rabbitmq/results/1_1consumer.txt &

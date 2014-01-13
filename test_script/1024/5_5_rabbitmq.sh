#!/bin/sh
stdbuf -oL python ../../rabbitmq/src/test_send.py &> ../../rabbitmq/results/256/5_5producer1.txt &
stdbuf -oL python ../../rabbitmq/src/test_send.py &> ../../rabbitmq/results/256/5_5producer2.txt &
stdbuf -oL python ../../rabbitmq/src/test_send.py &> ../../rabbitmq/results/256/5_5producer3.txt &
stdbuf -oL python ../../rabbitmq/src/test_send.py &> ../../rabbitmq/results/256/5_5producer4.txt &
stdbuf -oL python ../../rabbitmq/src/test_send.py &> ../../rabbitmq/results/256/5_5producer5.txt &
stdbuf -oL python ../../rabbitmq/src/test_receive_sync.py &> ../../rabbitmq/results/256/5_5consumer1.txt &
stdbuf -oL python ../../rabbitmq/src/test_receive_sync.py &> ../../rabbitmq/results/256/5_5consumer2.txt &
stdbuf -oL python ../../rabbitmq/src/test_receive_sync.py &> ../../rabbitmq/results/256/5_5consumer3.txt &
stdbuf -oL python ../../rabbitmq/src/test_receive_sync.py &> ../../rabbitmq/results/256/5_5consumer4.txt &
stdbuf -oL python ../../rabbitmq/src/test_receive_sync.py &> ../../rabbitmq/results/256/5_5consumer5.txt &

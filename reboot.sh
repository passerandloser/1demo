#!/usr/bin/env bash

echo -e "\033[34m-----------wsgi process----------------\033[0m"

ps -ef|grep 1demo_uwsgi.ini |grep -v grep

sleep 0.5

echo -e '\n------------going to close------------'

ps -ef |grep 1demo_uwsgi | grep -v grep | awk '{print $2}' | xargs kill -9

sleep 0.5

echo -e '\n------------check if the kill action is correct---------'

/envs/1demo/bin/uwsgi --ini 1demo_uwsgi.ini &  >/dev/null

echo  -e '\n\033[42;1m--------------started...-----------\033[0m'
sleep 1

ps -ef |grep 1demo_uwsgi.ini |grep -v grep
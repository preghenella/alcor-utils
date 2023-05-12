#! /usr/bin/env bash

if [ -x $1 ]; then
    echo "usage: start_masterlogic_server.sh [masterlogic]"
    exit
fi

COMMAND="/au/masterlogic/masterlogic_server.py --ml $1"
PIDLOCK="/tmp/masterlogic_server_ml$1.pid"

### check masterlogic server is running, otherwise start it
if [ $(ps -ef | grep masterlogic_server.py | grep "\-\-ml $1" | grep python3 | wc -l ) = "0" ]; then
    echo " --- masterlogic #$1 server not running: starting it "
    $COMMAND &> /tmp/masterlogic_server_ml$1.log &
    echo $! > $PIDLOCK
fi

COMMAND="/au/masterlogic/masterlogic_monitor.py --ml $1"
PIDLOCK="/tmp/masterlogic_monitor_ml$1.pid"

### check masterlogic monitor is running, otherwise start it
if [ $(ps -ef | grep masterlogic_monitor.py | grep "\-\-ml $1" | grep python3 | wc -l ) = "0" ]; then
    echo " --- masterlogic #$1 monitor not running: starting it "
    $COMMAND &> /tmp/masterlogic_monitor_ml$1.log &
    echo $! > $PIDLOCK
fi


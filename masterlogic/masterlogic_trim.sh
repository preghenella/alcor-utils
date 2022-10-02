#! /usr/bin/env bash

if [ -x $1 ] || [ -x $2 ]; then
    echo "usage: $0 [masterlogic] [channel]"
    exit 1
fi

timeout 1 /au/masterlogic/masterlogic_client.py --ml $1 --cmd "T $2 4080"
#!/usr/bin/bash
cd ../../src
if [ -e /usr/bin/python3 ]; then    
    ./main.py
else
    python ./main.py
fi

read end
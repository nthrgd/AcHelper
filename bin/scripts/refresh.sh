#!/usr/bin/bash
cd ../../src
if [ -e /usr/bin/python3 ]; then
    ./refresh.py
else
    python ./refresh.py
fi

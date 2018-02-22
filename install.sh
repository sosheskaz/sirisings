#!/bin/sh
pardir="$(dirname $0)"
cd "$pardir"
python2 -m pip install -r requirements.txt
cp sirisings/sirisings.py /usr/local/bin/sirisings

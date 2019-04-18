#!/bin/bash

# set -x
# set -e

sudo apt install python3-virtualenv
virtualenv venv -p /usr/bin/python2.7
chmod +x venv/bin/activate
source $PWD/venv/bin/activate
pip install -r requirements.txt

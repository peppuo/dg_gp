#!/bin/bash

alias pip="pip3"
alias python="python3"
alias run="python3 manage.py runserver $IP:$PORT"

pip3 install --upgrade pip
pip3 install -r requirements.txt

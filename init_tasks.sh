#!/bin/bash

echo 'alias pip="pip3"' >> ~/.bashrc
echo 'alias python="python3"' >> ~/.bashrc
echo 'alias run="python3 manage.py runserver $IP:$PORT"' >> ~/.bashrc
source ~/.bashrc

pip3 install --upgrade pip
pip3 install -r requirements.txt

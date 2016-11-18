#!/bin/sh

echo "----- Running server instance -----"
python registry.py runserver 0.0.0.0:$PORT

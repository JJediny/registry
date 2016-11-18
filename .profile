#!/bin/sh

echo "----- Setting up database -----"
python registry.py pycsw -c setup_db

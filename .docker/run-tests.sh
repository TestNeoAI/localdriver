#!/bin/bash
export DISPLAY=:1
cd /tests
python3 /playwright-setup/testrun.py

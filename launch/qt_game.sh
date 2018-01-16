#!/bin/bash

rosrun qt_make_demo packageMaker.py
rosrun qt_make_demo packageMod.py
rosrun qt_make_demo xmlToPy.py

echo Package successfully created. 
echo -----------------------------
echo You should now add images and voices to their respective folders.

#!/usr/bin/python

import roslib; roslib.load_manifest('qt_make_demo')
import rospy
import os

#Retrieve needed parameters
srcPath = rospy.get_param('/packageCreate/confPath')
packName = rospy.get_param('packName')

#Create the Image, Audio and launch files
os.chdir('/home/ciaran/catkin_ws/src/' + packName)
os.system('mkdir launch')
os.system('mkdir config')
os.chdir('/home/ciaran/catkin_ws/src/' + packName + '/config')
os.system('mkdir Audio')
os.system('mkdir Images')

#Copy the game.launch file into the launch folder
os.chdir(srcPath)
os.system('cp game.launch /home/ciaran/catkin_ws/src/' + packName + '/launch')

#Insert the package name in the game.launch file
os.chdir('/home/ciaran/catkin_ws/src/' + packName + '/launch')
os.system('sed -i \'s/xxx/' + packName + '/g\' game.launch')


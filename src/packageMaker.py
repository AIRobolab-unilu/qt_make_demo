#!/usr/bin/python

import roslib; roslib.load_manifest('qt_make_demo')
import rospy

import os

#Retrieves the needed parameters
print('\n-------------------------------------------------------')
packName = raw_input('What should the game-package be called? ')
print('-------------------------------------------------------\n')
srcPath = rospy.get_param('/packageCreate/confPath')

##Makes the package
os.chdir('/home/ciaran/catkin_ws/src')
os.system('catkin_create_pkg ' + packName + ' std_msgs rospy roscpp')

##Adds game.py and game.launch
os.chdir(srcPath)
os.system('cp gameTemplate.py /home/ciaran/catkin_ws/src/' + packName + '/src/game.py')

##Builds the workspace
os.chdir('/home/ciaran/catkin_ws')
os.system('catkin_make')

#Set parameters for the other nodes
rospy.set_param('destPath', '/home/ciaran/catkin_ws/src/' + packName + '/src/game.py')
rospy.set_param('packName', packName)

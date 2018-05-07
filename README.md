# qt_make_demo
## About
 A ROS package to create interactive demos on QT robot.

This package was developped as a bachelor semester project (BSP) for the first semester of the Bachelor in Computer Science (BiCS) of the university of Luxembourg and is an auxiliary part of qt_release (<https://github.com/fjrodl/qt_release>).
This package contains amongst others an **xml-parser** and is intended to be used to create packages with custom games based on face recognition for the robot to play. When launched, it automatically creates a package with a **game.py** file, already filled with the commands the user must enter into the xml-file, prior to running the package. The starting point of this package was the afore-mentioned xml parser, which reads data from an xml file and translates it into something the robot will understand and be able to execute. To be exact, it reads blocks tagged as *"action"*'s in the xml file and extracts the voices, gestures and faces to be made consequently and the duration to wait after each movement was completed.

---

## How to use
1. Write the desired actions into the **source.xml** file in the **config** directory. (The xml format is meant to facilitate the entry of this data.)

2. Run the package, by launching **qt_make_demo.launch**:

   `roslaunch qt_make_demo qt_make_demo.launch`

3. Enter the desired package-name when it prompts you.

4. Copy the trigger-images into the **config/Images** directory of the newly created package and rename them according to the prior entries in **source.xml**.

5. Copy the sound-files into the **config/Sounds** directory of the newly created package and rename them according to the prior entries in **source.xml**.

6. To run the new package, launch the game.launch file: 

   `roslaunch <your package> game.launch`

7. When the package is running, hold a print-out of your trigger-images in front of the camera. The robot will show the corresponding face and run the corresponding sound-file.

---

## Tree

![alt text](https://github.com/AIRobolab-unilu/qt_make_demo/blob/master/Tree.png"Dependency tree")

---

## LICENSE
Licensed under a BSD license (see LICENSE.bsd).

---

## Contributors
qt_release is developed by AI Robolab in the Computer Science and Communications Research Unit at University of Luxembourg.

This is a non-exhaustive list of contributors:

    fjrodl
    CiaranHagen


# qt_make_demo
ROS package to create demos on QT robot.
This package was developped as a bachelor semester project (BSP) for the first semester of the Bachelor in Computer Science (BiCS) of the university of Luxembourg.
This package contains amongst others an xml-parser and is intended to be used to create packages with custom games based on face recognition for the robot to play. When launched, it automatically creates a package with a game.py file, already filled with the commands the user must enter into the xml-file, prior to running the package. The starting point of this package was the afore-mentioned xml parser, which reads data from an xml file and translates it into something the robot will understand and be able to execute. To be exact, it reads blocks tagged as "action"'s in the xml file and extracts the voices, gestures and faces to be made consequently and the duration to wait after each movement was completed.
# LICENSE
Licensed under a BSD license (see LICENSE.bsd).
# Contributors
qt_release is developed by AI Robolab in the Computer Science and Communications Research Unit at University of Luxembourg.

This is a non-exhaustive list of contributors:

    fjrodl
    CiaranHagen


#!/usr/bin/python

import roslib; roslib.load_manifest('qt_make_demo')
import rospy

from lxml import etree
from io import BytesIO
import os

destPath = rospy.get_param('destPath')
        
##Gets filepaths
srcPath = rospy.get_param('/packageCreate/srcPath')

#----------------------------------------------------------------------
def parseXML(xmlFile, strL):
    """
    Parse the xml file
    Appends the data from the .xml file to strL in context.
    """
    f = open(xmlFile)
    xml = f.read()
    f.close()
    tree = etree.parse(BytesIO(xml.encode('utf-8')))
    data = tree.getroot()
    blockID = '0'
    for action in data:
        if action.get('id') == '1':
            blockID = action.get('id')
            strL.append('                    if image_id == %s :' % blockID)
        elif int(action.get('id'))>1:
            blockID = action.get('id')
            strL.append('                    elif image_id == %s :' % blockID)

        for elem in action:
            if (not elem.text):
                text = None
            else:
                text = elem.text
        for i in range(len(action)):
            if action[i].tag == 'face':
                if (not action[i].text):
                    text = None
                else:
                    text = action[i].text 
                    text2 = action[i+1].text
                    if text2 != 'NOSOUND':
                        strL.append('                        self.face_and_sound_call("%s", %s)' %(text, text2))
                    elif text2 == 'NOSOUND':
                        strL.append('                        self.face_and_sound_call("%s", "%s")' %(text, text2))
            if action[i].tag == 'gesture':
                if (not action[i].text):
                    text = None
                else:
                    text = action[i].text 
                    strL.append('                        v_gesture = "%s"\n                        self.gesture_player_pub.publish(v_gesture)' %text)

            if action[i].tag == 'duration':
                if (not action[i].text):
                    text = None
                else:
                    text = action[i].text
                    strL.append('                        rospy.sleep(' + text + ')')
			
    if blockID == '0':
        print('Nothing in xml file.')
		
##Putting code before 'insert part' into strL and the rest into strL2
dest = open(destPath,'r')

strL = []
strL2 = []
strL = dest.read().splitlines()
for s in strL:
    if s == '                    ##START Commands##':
        strL2 = strL[strL.index(s)+1:]
        strL = strL[:strL.index(s)+1]
dest.close()

##Putting 'insert part' into list
if strL2 != []:
    if __name__ == "__main__":
        parseXML(srcPath, strL)

##Concatenates lists
strL = strL + strL2

strL = [s + '\n' for s in strL]

##Writes to file.py              
dest = open(destPath,'w')
dest.writelines(strL)
dest.close()
        

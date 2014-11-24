import clr
import sys

InitalPath = "C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\Robot Application Builder 5.12\\PC SDK\\";

clr.AddReferenceToFileAndPath(InitalPath + 'ABB.Robotics.Controllers.dll');
clr.AddReferenceToFileAndPath(InitalPath + 'ABB.Robotics.dll');

import ABB.Robotics.Controllers as control
import ABB.Robotics as robot

def FindDir(Dir):

	return dir(eval(Dir));

lambda x: FindDir(x)
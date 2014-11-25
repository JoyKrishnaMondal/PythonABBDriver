#PythonABBDriver
An attempt to create an open python interface to allow accessing functionality of IRB series ABB robots via terminal

## CrashCourse on the ABB software system

1. ABB is a microsoft shop, they have exposed their SDK using 2 <code>.DLL</code> files.

2. ABB robots cannot be directly controlled, the robot is connected to another piece of hardware called the controller - we can only talk to this controller. The flexpendent is the console/terminal/screen to this hardware.

3. ABB has written a Domain Specfic Language for their robots. The <code>.DLL</code> has no function that can be directly called to make the robot do things. This Domain specifc language is called <code>RAPID</code>.


4. We can only make the controller execute RAPID code. It will not execute C#,C++ or any other mainstream language that you are used to.

5. The SDK only allows us to upload, manipulate and remove RAPID code using the <code>.DLL</code>s.

## Aim of project

I have started this project to attempt to create an interface in ironpython that will allow to me sent instructions onto a TCP/IP socket to ironpython that will use ABB's SDK to upload relevant RAPID code or at least manipulate it so that we can in a simple manner make the robot do things we want it to.

## Progress

1. The code I have until now will allow you to easily upload a sample rapid code to execute on the robot.


##TODO

1. Access the robot's functionality via MATLAB and javascript (node.js)






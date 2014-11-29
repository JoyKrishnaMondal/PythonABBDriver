class dotdict(dict):
     def __getattr__(self, attr):
         return self.get(attr)
     __setattr__= dict.__setitem__
     __delattr__= dict.__delitem__

import System
import clr
import sys
import os
clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.dll')
clr.AddReferenceToFileAndPath('ABB.Robotics.dll')
import ABB.Robotics.Controllers as control
import ABB.Robotics as robot

def printf(string,color = "Green",EndLine = True):
	
	System.Console.ForegroundColor = eval("System.ConsoleColor." + color)
	System.Console.Write(string)
	if (EndLine == True):
		System.Console.Write("\n")
	System.Console.ResetColor()

def Initiate():

	InitalPath = os.getcwd()

	scanner = control.Discovery.NetworkScanner()

	scanner.Scan()

	printf("scan complete")

	controllers = control.ControllerInfoCollection()

	controllers = scanner.Controllers

	printf (str(controllers.Count),EndLine = False)

	printf(" ABB Robots found in network")

	VirtualController = controllers[0]
	VirtualController = control.ControllerFactory.CreateFrom(VirtualController)
	VirtualController.Logon(control.UserInfo.DefaultUser)

	printf("logged on to virtual controller")

	m = control.Mastership.Request(VirtualController.Rapid)

	printf("MasterShip granted")

	VirtualController.AuthenticationSystem.CheckDemandGrant(control.Grant.ExecuteRapid)

	printf("Authentication Granted to run Rapid Code")

	tRob1 = VirtualController.Rapid.GetTask("T_ROB1")
	
	filename  = "helloworld.mod"

	home = VirtualController.GetEnvironmentVariable("HOME")

	VirtualController.FileSystem.RemoteDirectory = home
	VirtualController.FileSystem.LocalDirectory = InitalPath
	VirtualController.FileSystem.PutFile(filename, filename, True)
	tRob1.LoadModuleFromFile(home + "/" + filename,control.RapidDomain.RapidLoadMode.Replace)
	tRob1.SetProgramPointer("MainModule", "main")
	# tRob1.Start()
	VirtualController.Rapid.Start()




	# tRob1.LoadModuleFromFile("T_ROB1\\MainModule\\main\\NewProgramName.mod",control.RapidDomain.RapidLoadMode.Replace)




	# p20 = VirtualController.Rapid.GetRapidData("T_ROB1", "MainModule","p20")



	# def handle(*args):

	# 	print args[0].Value.ToString()

	# p20.ValueChanged += handle
	# # print p20.Value.ToString()


	# def MoveBy(x = 90):

	# 	Amount = VirtualController.Rapid.GetRapidData("T_ROB1", "MainModule","Amount")
	# 	AmountChange = control.RapidDomain.Num()
	# 	AmountChange.Value = x

	# 	Amount = AmountChange
	# 	print Amount.Value.ToString()

	# 	VirtualController.Rapid.Start()


	# def EndSession():
	# 	print "Disconnecting From Arm"
	# m.Release()
	VirtualController.Logoff()
	VirtualController.Dispose()


	# return dotdict({"MoveBy":MoveBy, "EndSession":EndSession})


try:
	Initiate()
except Exception as e:
	printf(e,"Red")
	# printf (Runtime)

# Fn.MoveBy()

# Fn.EndSession()



# RD = control.RapidDomain.RapidData()

# from threading import Timer

# def setTimeout(x):
# 	print x
# 	r = Timer(1.0, setTimeout, ("HelloWorld",))
# 	r.start()

# setTimeout("Start")

# RapidData rd = VirtualController.Rapid.GetRapidData("T_ROB1", "MainModule", "Amount");


# print VirtualController.EventLog.GetCategories()[0]

# print dir(control.RapidDomain)

# lambda x: FindDir(x)


# print FindDir("robot")


# from time import sleep
# while True:
# 	sleep(1)


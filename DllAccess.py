class dotdict(dict):
     def __getattr__(self, attr):
         return self.get(attr)
     __setattr__= dict.__setitem__
     __delattr__= dict.__delitem__

White = "\033[0;37m"

LightGreen = "\033[1;32m"

Green = "\033[0;32m"

def Initiate():

	import clr
	import sys
	import System


	InitalPath = "C:\\usb\\"

	clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.dll')
	clr.AddReferenceToFileAndPath('ABB.Robotics.dll')

	import ABB.Robotics.Controllers as control
	import ABB.Robotics as robot

	print "start scan"

	scanner = control.Discovery.NetworkScanner()

	scanner.Scan()

	print "scanned"

	controllers = control.ControllerInfoCollection()

	controllers = scanner.Controllers
	print (controllers.Count)
	VirtualController = controllers[0]
	VirtualController = control.ControllerFactory.CreateFrom(VirtualController)
	VirtualController.Logon(control.UserInfo.DefaultUser)
	print "logged on to virtual controller"
	m = control.Mastership.Request(VirtualController.Rapid)
	# def handle(*args):
	# 	print args
	VirtualController.AuthenticationSystem.CheckDemandGrant(control.Grant.ExecuteRapid)
	print "Authentication Granted to run Rapid Code"
	tRob1 = VirtualController.Rapid.GetTask("T_ROB1")
	filename  = "helloworld.mod"
	home = VirtualController.GetEnvironmentVariable("HOME")
	VirtualController.FileSystem.RemoteDirectory = home
	VirtualController.FileSystem.LocalDirectory = "C:/usb"
	VirtualController.FileSystem.PutFile(filename, filename, True)
	# VirtualController.Rapid.ResetProgramPointer()
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



Fn = Initiate()

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


class dotdict(dict):
     def __getattr__(self, attr):
         return self.get(attr)
     __setattr__= dict.__setitem__
     __delattr__= dict.__delitem__

def Initiate():

	import clr
	import sys


	InitalPath = "C:\\usb\\"

	clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.dll')
	clr.AddReferenceToFileAndPath('ABB.Robotics.dll')

	import ABB.Robotics.Controllers as control
	import ABB.Robotics as robot


	scanner = control.Discovery.NetworkScanner()

	scanner.Scan()

	controllers = control.ControllerInfoCollection()

	controllers = scanner.Controllers
	# print scanner.Controllers[0]
	VirtualController = controllers[0]
	VirtualController = control.ControllerFactory.CreateFrom(VirtualController)

	VirtualController.Logon(control.UserInfo.DefaultUser)

	m = control.Mastership.Request(VirtualController.Rapid)

	def handle(*args):
		print args

	VirtualController.AuthenticationSystem.CheckDemandGrant(control.Grant.ExecuteRapid)

	tRob1 = VirtualController.Rapid.GetTask("T_ROB1")

	# print (VirtualController.FileSystem.GetLocalPath)
	# print (VirtualController.FileSystem.GetRemotePath)
	# print dir (VirtualController.FileSystem)
	# print (VirtualController.FileSystem.BeginListDirectory(,handle))

	# GetMasterRapid
	# VirtualController.FileSystem.PutFile("C:\\usb\\helloworld.mod",True)

	localdir = VirtualController.FileSystem.LocalDirectory
	remotedir = VirtualController.FileSystem.RemoteDirectory

	print localdir
	print remotedir

	tRob1.LoadModuleFromFile("C:\\usb\\helloworld.mod",control.RapidDomain.RapidLoadMode.Replace)
	tRob1.SetProgramPointer("MainModule", "main")
	VirtualController.Rapid.Start()

	# VirtualController.Rapid.ResetProgramPointer()


	# tRob1.LoadModuleFromFile("T_ROB1\\MainModule\\main\\NewProgramName.mod",control.RapidDomain.RapidLoadMode.Replace)



	# tRob1.Start()

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
	m.Release()
	VirtualController.Logoff()


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


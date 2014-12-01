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
import re 
def printf(string,color = "Green",EndLine = True):

	System.Console.ForegroundColor = eval("System.ConsoleColor." + color)
	System.Console.Write(string)
	if (EndLine == True):
		System.Console.Write("\n")
	System.Console.ResetColor()

def handle(*args):
		printf("Current XYZ/Queternion:",EndLine = False)
		printf (args[0].Value.ToString())

def ValueChanged(name):

	def ReturnFn (*args):
		printf(name,EndLine = False)
		printf(" Changed:",EndLine = False)
		printf(args[0].Value.ToString())

	return ReturnFn

def RegexChange(value = "0,0,0",name="p20",filename ="helloworld.mod"):

	f = open(filename,'r')

	readData = f.read()
	

	ReString = 'Offs\(' + name + ",(.*)\);"
	Replace = 'Offs(' + value + ");"

	replaced = re.sub(ReString,Replace,readData);
	# o.write(replaced)
	
	f.close()
	o = open(filename,'w')
	o.write(replaced)
	o.close()

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
	p20 = VirtualController.Rapid.GetRapidData("T_ROB1", "MainModule","p20")
	p20.ValueChanged += handle

	m.Release()
	m.Dispose()
	# VirtualController.Rapid.GetRapidData("T_ROB1", "MainModule","Amount").ValueChanged += handle
	# print p20.Value.ToString()


	def MoveBy(x = 0):


		Amount = VirtualController.Rapid.GetRapidData("T_ROB1", "MainModule","Amount")


		AmountChange = control.RapidDomain.Num()
		AmountChange.Value = x



		# change = control.RapidDomain.RapidData(VirtualController,Amount)

		m = control.Mastership.Request(VirtualController.Rapid)

		Amount = AmountChange
		# Amount.Value = x
		m.Release()
		m.Dispose()

		# change = control.RapidDomain.IRapidData.Fill(str(x))

		# Amount.WriteItem(change,0)
		# m.Release()
		# m.Dispose()
		# VirtualController.Rapid.Start()

		print x
		Amount = VirtualController.Rapid.GetRapidData("T_ROB1", "MainModule","Amount")
		print Amount.Value.ToString()
		# raw_input()
		# printf("Amount = ",EndLine = False)
		# printf( Amount.Value.ToString())



	def EndSession():
		printf("Disconnecting From Arm")
		# m.Release()
		VirtualController.Logoff()
		VirtualController.Dispose()


	return dotdict({"MoveBy":MoveBy, "EndSession":EndSession})


try:
	RegexChange(sys.argv[1])
	Fn = Initiate()
	# Fn.MoveBy(10.0)

	# from time import sleep
	printf("Press Enter to End . .")
	raw_input()
	Fn.EndSession()


except Exception as e:
	printf(e,"Red")

	# printf (Runtime)

# Fn.MoveBy()




# print VirtualController.EventLog.GetCategories()[0]



# lambda x: FindDir(x)








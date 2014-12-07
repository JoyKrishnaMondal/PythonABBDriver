edge = require "edge"
fs = require "fs"
{reduce} = require "underscore"
{zip-with,map} = require "prelude-ls"
{usleep} = require "sleep"


White = "\033[0;37m"
LightGreen = "\033[1;32m"
Green = "\033[0;32m"
RedLight = "\033[0;31m"
Red = "\033[1;31m"
Brown = "\033[0;33m"

log =(string)-> console.log Brown + "JS: " + string + White

AccessFn = edge.func "py", "block.py"
Main = {}
Main.ChangeCount = true
MatlabFile = "MoveRobot.txt"
ExchangeFile = "Exchange.json"
HomeFile = "Home.txt"



GetExchange = ->
	data = fs.readFileSync ExchangeFile
	JSON.parse data

SetExchange =(string) ->
	fs.writeFileSync ExchangeFile,(JSON.stringify (string))

TouchExchange = -> SetExchange (GetExchange!)

E = GetExchange!
E.RobotDone = true
SetExchange E

cleanUp = -> AccessFn "EndSession()",(err,result) ->
	if err 
		throw err

	process.exit!

process.on "SIGINT",cleanUp


MatlabInput = (Input)->

	Vector = Input
	Vector = Vector.slice 1, (Vector.length-1)

	if (!(/,/.test Vector ))
		Vector = Vector.replace /\s/g,","

	Vector

RunRobot  = (Vector) ->

	fs.writeFileSync "hello.txt",Vector
	PassString = "MoveBy(" + "'" + Vector + "'" + ")"

	start = new Date!.getTime!

	log LightGreen + PassString

	AccessFn PassString,(err,result)->

		if err 
			console.log err

		end = new Date!.getTime!
		time = end - start
		log Green + "Execution took: " + LightGreen + time + Green + " milliseconds."

fs.watch MatlabFile,(err)->
	
	Main.ChangeCount = !Main.ChangeCount

	if Main.ChangeCount == true

		data = fs.readFileSync MatlabFile
		Vector = data.toString!
		log Brown + "MATLAB" + Green +  " calling . ."
		RunRobot MatlabInput Vector




MatrixToString  = (input = [1,2,3]) ->

	ST = input.toString!

	ST.slice 0, (ST.length)

StringToMatrix = (input =" 1,2,3") ->

	# console.log input
	XYZ = (/(.*),(.*),(.*)/.exec input)[1 to 3]
	XYZ.map (x)-> parseFloat x


GetHomeMatrix = -> StringToMatrix ((fs.readFileSync HomeFile).toString!)

SetHomeMatrix =(Matrix) -> fs.writeFileSync HomeFile, Matrix.toString!
AddMomentHistory = (M = [-1,2,3]) ->
	
	Added = (zip-with (+), M, GetHomeMatrix!)
	SetHomeMatrix Added

GoHome = -> 
	RunRobot map (*(-1)) , GetHomeMatrix!
	SetHomeMatrix [0,0,0]






SequenceRepeat = (seq = [[0,0,30],[0,-30,-30]] ,Repeat = 1)->

	I = 0 
	Main.Exchange = true
	OverallSteps = Repeat*seq.length
	watcher = fs.watch ExchangeFile,(err)->
		Main.Exchange = !(Main.Exchange)
		if Main.Exchange
			Json = GetExchange!
			if Json.RobotDone
				if I == OverallSteps
					log LightGreen + "GoHome()"
					GoHome!
					setTimeout (-> watcher.close!),0
				else
					M = seq[I%seq.length]
					RunRobot MatrixToString M
					AddMomentHistory M
					I++
					

	# usleep 13000000 
	
# RunRobot MatrixToString [0,0,-30]
try
	seq = [[0,0,30],[0,30,30]]
	# seq = [[0,0,30],[0,-30,-30]]
	SequenceRepeat seq
	TouchExchange!
	# setTimeout (()-> fs.writeFileSync ExchangeFile , (fs.readFileSync ExchangeFile)) ,0

catch ER
	console.log Red + ER + White
	cleanUp!


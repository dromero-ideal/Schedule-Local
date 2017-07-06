from modules.Schedule_FilePaths import *
from modules.Schedule_Classes import *
from Import_Rosters import *


###################################################################################################################

def MasterSchedule(saveFile):
	master = []
	for c in CourseList:
		master.append(c.period)
	ms = open(saveFile, 'a')
	ms.write(", ".join(str(j) for j in master))
	ms.write("\n")
	ms.close()

###################################################################################################################

def HumanReadableSchedule(saveFile):
	hrs = open(saveFile, 'w')
	for i in range(nPeriods+1):
		hrs.write("Period {0}\n".format(i))
		for c in CourseList:
			if c.period == i:
				hrs.write("{0}\n".format(c.name))
		hrs.write("\n")
	hrs.write("!!!!!!!!!!WIN!!!!!!!!!!\n\n")

	for s in Students:
		hrs.write("{0}\n".format(s.name))
		hrs.write("-----------------\n")
		s.schedule.sort(key = getPeriod)
		for c in s.schedule:
			hrs.write("{0} - {1}\n".format(c.period, c.name))
		hrs.write("\n")
	hrs.write("\n")
	hrs.close()

###################################################################################################################

def StudyHall(saveFile1, saveFile2, saveFile3):
	sh = open(saveFile1, 'w')
	for i in range(1,nPeriods+1):
		sh.write("Period {0} \n".format(i))
		for p in Students:
			if p.period[i] == 0:
				sh.write("{0} \n".format(p.name))
		sh.write("\n\n")
	sh.close()

	msSh = open(saveFile2, 'w')
	for i in range(1,nPeriods+1):
		msSh.write("Period {0} \n".format(i))
		for p in msStudents:
			if p.period[i] == 0:
				msSh.write("{0} \n".format(p.name))
		msSh.write("\n\n")
	msSh.close()

	hsSh = open(saveFile3, 'w')
	for i in range(1,nPeriods+1):
		hsSh.write("Period {0} \n".format(i))
		for p in hsStudents:
			if p.period[i] == 0:
				hsSh.write("{0} \n".format(p.name))
		hsSh.write("\n\n")
	hsSh.close()

###################################################################################################################

def lastAttempt():
	for c in PCourseList:
		if c.period == 0:
			return c.previousCourse
	return PCourseList[len(PCourseList)-1]
#Returns which course was the last to be assigned a period.
###################################################################################################################

def ProgressMonitor(nMon,nMonMax):
	if nMon < nMonMax:
		return nMon + 1
	else:
		#periodList = []
		#for c in PCourseList:
		#	periodList.append(c.period)
		print(periodList)
		return 0

###################################################################################################################

#Assign the n-th class and higher.
#The first course nStart will be assigned starting with nPeriod.
#The following courses will be assigned starting with period 1.
nMonitor = 0
def MasterAssign(nStart,nPeriod,outputType):
	#Get the course object and the number of courses.
	cC = PCourseList[nStart]
	nC = len(PCourseList)
	#Print updates to console
	global nMonitor
	nMonitorMax = 10**6 #Number loops before displaying progress.
	nMonitor = ProgressMonitor(nMonitor,nMonitorMax)

	#Main part of function.
	if cC.period == 0:
		proceed = cC.Assign(nPeriod)
		if proceed == True:
			if nStart < nC-1:
				#print("Working on {0}".format(PCourseList[nStart+1].name))
				return MasterAssign(nStart+1,1,outputType)
			elif nStart == nC-1:

				if outputType == "Master":
					#export schedule in some useable csv file
					MasterSchedule(solutionsCSV)
					restartPeriod = cC.period
					cC.UnAssign()
					return MasterAssign(nStart,restartPeriod+1,outputType)

				elif outputType == "Formatted":
					HumanReadableSchedule(solution)
					StudyHall(studyHall)
					print("!!!!!!!!!!WIN!!!!!!!!!!")
					return True

				else:
					print("Output Type not recognized.")
					return "Output Type not recognized."

			else:
				print("Possible Error. No more courses to assign.")
				return "Possible Error. No more courses to assign."
		elif proceed == False:
			return False

		else:
			print("Assign function not behaving properly.")
			return "Assign function not behaving properly."      
	else:
		if nStart < nC-1:
			print("Error: {0} is already assigned to period {1}".format(cC.name,cC.period))
			return MasterAssign(nStart+1,1,outputType)
		else:
			restartPeriod = cC.period #Move course up one period.
			cC.UnAssign()
			print("Is this working? Why are all courses assigned and program is not done?") #This should never happen.
			return MasterAssign(nStart,restartPeriod+1,outputType) #Move course up one period.

###################################################################################################################

#modified to include bigger jumps
#The program will not reassign any courses before halt. 
#Ex. if halt = 5, then periods 0-4 are set in stone on their first pass.
#Only usefull if you know a solution. Default is halt = 0.
def Continue(outputType, halt):
	#print("Continue")

	#periodList = []
	#for c in PCourseList:
	#	periodList.append(c.period)
	previousPeriodList = periodList[:]

	last = lastAttempt()
	if last == False: #Prevent from reassigning courses lower than this.
		print("Schedule is finished.")
		g = open(solutionsCSV, 'a')
		g.write("Schedule is finished.")
		g.close()
		return True

	jumpCounter = last.UnAssign()-1
	#print(jumpCounter)
	k = last.i-jumpCounter
	#print(k)

	#print("jump = {0} class {1} period {2}".format(jumpCounter, k, periodlist[k]+1))
	#Need the PeriodList[] before running UnAssign             
	return MasterAssign(k, previousPeriodList[k]+1,outputType)

###################################################################################################################
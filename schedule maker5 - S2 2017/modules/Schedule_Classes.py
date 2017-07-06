import math

nPeriods = 10
#All courses must be added before adding students.
##################################################################################################################
#Courses
##################################################################################################################
CourseList  = []     #CourseList is for Output.
PCourseList = []    #PCourseList is to optimize.
periodList  = []
#Creating class to contain information on courses.
class Course:
	#Student and Teachers
	def __init__(self, Name):
		self.name = Name
		#Default Perameters
		self.period = 0 #Zero period means course is waiting for assignment.
		self.people = [] #Person objects placed here corresponding to a roster (includes teachers and rooms).
		self.priority = 0 #Set order for All Courses. High priority goes first.
		self.conflictCount = 0 #Number of courses in potential conflict with this one.

		CourseList.append(self)
		self.i = False #index in PCourseList
		self.previousCourse = False #Save course that comes before in PCourseList. 
		#This can be used to find which course was assigned just before this course.

		self.isPT = False #Is this the higest priorty course for a any part-time teacher?

	#Check if a group of students is free during nth period. 0th period is a place holder and is always free.
	def free(self, n):
		return all(p.period[n] == 0 for p in self.people)

	#Assign students as busy during a certain period.
	def AssignPeople(self,n):
		for p in self.people:
			p.period[n] += 1
			if p.period[n] > 1:
				print("ERROR {} is overbooked.".format(p.name))

	#Part Time rewritten.
	#After successful add or drop. Assign = 1. UnAssign = 0
	def PartTime(self,n,AorU):
		MWF = [1,2,3,4,5]
		TR  = [6,7,8,9]
		for pt in PartTime:
			if pt in self.people:
				if n in MWF:
					for i in TR:
						if i < nPeriods+1:
							pt.period[i] = AorU
					#print("{0} {1} modified {2}".format(pt.name, AorU, pt.period))
				elif n in TR:
					for i in MWF:
						if i < nPeriods+1:
							pt.period[i] = AorU
					#print("{0} {1} modified {2}".format(pt.name, AorU, pt.period))
				else:
					print("Error in PartTime Function")

	#Check if members of the i-th course are free during n-th period.
	#If True assign that period to the course and show students as busy.
	#If Fasle check for period n+1
	def Assign(self,n):
		#3-fold Symmetry 1,2,3
		# if n == 1:
		# 	#print("Symettry Check 1")
		# 	#periodList = []
		# 	#for c in PCourseList:
		# 	#	periodList.append(c.period)
		# 	#print(periodList)
		# 	# if  3 not in periodList:
		# 	# 	#print("Skip to 3")
		# 	# 	n = 3
		# 	#elif 2 not in periodList:
		# 	if 2 not in periodList:
		# 		#print("Skip to 2")
		# 		n = 2

		#2-fold Symmetry 6,7
		#elif n == 6:
		if n == 6:
			#print("Symettry Check 6")
			#periodList = []
			#for c in PCourseList:
			#	periodList.append(c.period)
			#print(periodList)
			if  7 not in periodList:
				#print("Skip to 7")
				n = 7		

		#Check that n is in bounds.
		if n == 0:
			#Assign should never be used this way.
			print("Assign Period should not be assigned to 0")
			return "Assign Period should not be assigned to 0"
		elif n > nPeriods:
			#print("No available periods for {0}".format(self.name))
			return False

		#Main part of function
		else:
			if self.free(n):
				self.period = n
				periodList.append(n)
				self.AssignPeople(n)
				#print("{0} is assigned to period {1}".format(self.name,n))
				#Part-Time Assign
				if self.isPT:
					self.PartTime(n, 1)
				return True

			else:
				if n < nPeriods:
					#print("{0} has conflict with period {1}. Checking period {2}".format(self.name, n, n+1))
					return self.Assign(n+1)
				elif n == nPeriods:
					#print("{0} has conflict with period {1}".format(self.name, n))
					return False
				else:
					print("Period is out of bounds")
					return "Period is out of bounds"

	#Check if members of the i-th course are free during n-th period.
	#If True assign that period to the course and show students as busy.
	#If Fasle check for period n+1
	def SlowAssign(self,n):
		#Check that n is in bounds.
		if n == 0:
			#Assign should never be used this way.
			print("Assign Period should not be assigned to 0")
			return "Assign Period should not be assigned to 0"
		elif n > nPeriods:
			#print("No available periods for {0}".format(self.name))
			return False

		#Main part of function
		else:
			if self.free(n):
				self.period = n
				periodList.append(n)
				self.AssignPeople(n)
				#print("{0} is assigned to period {1}".format(self.name,n))
				#Part-Time Assign
				if self.isPT:
					self.PartTime(n, 1)
				return True

			else:
				if n < nPeriods:
					#print("{0} has conflict with period {1}. Checking period {2}".format(self.name, n, n+1))
					return self.Assign(n+1)
				elif n == nPeriods:
					#print("{0} has conflict with period {1}".format(self.name, n))
					return False
				else:
					print("Period is out of bounds")
					return "Period is out of bounds"

	#Remove course period assignment as necessary.
	#Jump is used in continue function.
	def UnAssign(self):
		jump = 1

		#Check if course is at last period. If so also unassign last class.
		if self.period > nPeriods-1 and self.previousCourse != False: 
			jump += self.previousCourse.UnAssign()
		
		#UnAssign all people in this course.
		for p in self.people:
			p.period[self.period] = 0
		#Free up Part-Time if this is their first course.
		if self.isPT:
			self.PartTime(self.period, 0)

		#UnAssign this course.
		self.period = 0
		periodList.pop()
		return jump

	#Prioritize Courses by how many students and how rigid those students schedules are
	def setPriority(self):
		xp = 0
		for p in self.people:
			xp += 10**p.scheduleLength
		self.priority = 2*math.log(xp)

	def countConflicts(self):
		count = 0
		for c in CourseList:
			if any(p in c.people for p in self.people):
				count +=1
		self.conflictCount = count

def getPriority(c):
	return c.priority
def getConflictCount(c):
	return c.conflictCount
def getOrder(c):
	return c.priority + c.conflictCount
def getPeriod(c):
	return c.period


##################################################################################################################
#People
##################################################################################################################
AllPeople = []
Teachers = []
FullTime = []
PartTime = []
Rooms = []
Students = []
msStudents = []
hsStudents = []
#Creating class to contain information on teachers and students.
class Person:
	#Student and Teachers
	def __init__(self, Name, pType):
		self.name = Name
		self.pType = pType
		#Default Perameters
		self.schedule = [] #Course objects placed here.
		self.scheduleLength = 0
		self.course = [0]*len(CourseList) #List of 0 or 1's corresponding to enrollement to a certain course.
		self.period = [0]*(nPeriods+1) #Zero period should be left empty. Set the number of periods.

		AllPeople.append(self)
		if pType == 'msStudent':
			msStudents.append(self)
			Students.append(self)
		elif pType == 'hsStudent':
			hsStudents.append(self)
			Students.append(self)
		elif pType == 'T':
			FullTime.append(self)
			Teachers.append(self)
		elif pType == 'P':
			PartTime.append(self)
			Teachers.append(self)
		elif pType == 'R':
			Rooms.append(self)

	#Return the number of courses a student is taking.
	#Modified to use unavailable periods to increase priority.
	def setScheduleLength(self):
		self.scheduleLength = len(self.schedule) + 20*((sum(self.period) + 1)//nPeriods)
		return self.scheduleLength


##################################################################################################################
#Functions for People and Courses
##################################################################################################################
#This section is obsolete.
#Take classes from student's schedule to their courselist.
# def ScheduleConstructor(student):
# 	for i in range(len(CourseList)):
# 		if CourseList[i] in student.schedule:
# 			student.course[i] = 1
# 		else:
# 			student.course[i] = 0
# #Run ScheduleConstructor for all Students
# def AllScheduleConstructor():
# 	for p in AllPeople:
# 		ScheduleConstructor(p)

##################################################################################################################

#Functions to Construct Courses and Rosters.
#Add students to a Course
def CourseConstructor(c):
	c.people = []
	for p in AllPeople:
		if c in p.schedule:     #Go by .schedule
		#if p.course[n]:        #Go by .course
			c.people.append(p)
#Run CourseConstructor for all Courses
def AllCourseConstructor():
	for c in CourseList:
		CourseConstructor(c)

#Algorithm for creating PCourseList.
#In other words prioritizing courses for assignment.

def PrioritizedCourseListConstructor():
	#This needs to be run after all people and courses are added.
	for p in AllPeople:
		p.setScheduleLength()
	for c in CourseList:
		c.setPriority()
		c.countConflicts()
	#PCourseList is empty. Adding a sorted version of CourseList
	PCourseList.extend(sorted(CourseList, key = getOrder, reverse = True))
	
	#Each course needs to know which course comes before or if it is the first.
	for i in range(len(PCourseList)):
		PCourseList[i].i = i
		#periodList.append(PCourseList[i].i.period)
		if i > 0:
			PCourseList[i].previousCourse = PCourseList[i-1]

def PartTimeConstructor():
	for p in PartTime:
		ptCourseList = sorted(p.schedule, key = getOrder, reverse = True)
		ptCourseList[0].isPT = True


###################################################################################################################

def Constructor():
	#AllScheduleConstructor()
	AllCourseConstructor()
	PrioritizedCourseListConstructor()
	PartTimeConstructor()

###################################################################################################################

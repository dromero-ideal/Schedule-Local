from modules.Schedule_FilePaths import *
from modules.Schedule_Classes import *
import csv


#For adding all COURSES.
#Check if row contains a teacher. 
#Store all values except grade, name and blanks.
#################################################
lastNameCol  = 0 #First 3 Columns
firstNameCol = 1
typeCol      = 2
firstCourseCol = typeCol + 1 # 11 Course Columns after first 3 Colums
lastCourseCol  = typeCol + 11
firstPeriodCol = lastCourseCol + 2 #Skip Load Column. 9 Periods after courses
#lastPeriodCol  = lastCourseCol + 9
#################################################
with open(inputCSV, 'r') as csvfile:
	rosters = csv.reader(csvfile)

	next(rosters)
	for row in rosters:
		if row[typeCol] in ['T', 'P']:
			for i in range(firstCourseCol, lastCourseCol+1):
				if  row[i] != '':
					if all(row[i] != c.name for c in CourseList):
						newCourse = Course(row[i])
					else:
						print('Duplicate Course {0}'.format(row[i]))

#################################################
#For adding all PEOPLE.
#Grab their grade and name. Create new person.
#################################################
with open(inputCSV, 'r') as csvfile:
	rosters = csv.reader(csvfile)

	next(rosters)
	for row in rosters:
		if row[typeCol] != '':
			
			if row[typeCol] in ['6','7','8']:
				name = row[lastNameCol] + ', ' + row[firstNameCol]
				pType = 'msStudent'
			elif row[typeCol] in ['9','10','11','12']:
				name = row[lastNameCol] + ', ' + row[firstNameCol]
				pType = 'hsStudent'
			elif row[typeCol] in ['T','P','R']:
				name = row[lastNameCol]
				pType = row[typeCol]
			else:
				print("Type Column Error")

			print(name)
			newPerson = Person(name, pType)
			for i in range(firstCourseCol, lastCourseCol+1):
				if  row[i] != '':
					if all(row[i] != c.name for c in CourseList):
						print("Error {0} for {1} is not found in CourseList".format(row[i], newPerson.name))
					else:
						for c in CourseList:
							if row[i] == c.name:
								#print("Added {0} to {1}.".format(c.name, newPerson.name))
								newPerson.schedule.append(c)
			if row[typeCol] in ['T','P','R']:
				for i in range(nPeriods): #For each period
					newPerson.period[i+1] = int(row[i+firstPeriodCol]) 
					#(i+1) because we start at period 1. 
					#(i+firstPeriodCol) because we start at firstPeriodCol in spreadsheet.
				#print(newPerson.period)


#################################################
#Take classes from student's schedule to their courselist.
#Add students to a Course
Constructor()
#################################################
#print('Test Output')
#For checking results of import.
##################################################
#Courses *No Longer sure what this does.*
# with open(inputCSV, 'r') as csvfile:
# 	rosters = csv.reader(csvfile)
# 	next(rosters)
# 	for row in rosters:
# 		if row[2] in ['T', 'P']:
# 			for i in range(3, len(row)):
# 				if  row[i] != '':
# 					print(row[i])
# print('\nCourseList\n')
# for c in CourseList:
# 	print(c.name, c.period)

#PCourseList: Order in which courses are set.
print('\nPCourseList\n')
for c in PCourseList:
	if c.previousCourse == False:
		print(repr(c.period).rjust(1), ('%.2f' %(c.conflictCount+c.priority)).rjust(7), repr(c.conflictCount).rjust(3), ('%.2f' %(c.priority)).rjust(6), '', c.name.ljust(32), repr(c.i).rjust(2))
	else:
		print(repr(c.period).rjust(1), ('%.2f' %(c.conflictCount+c.priority)).rjust(7), repr(c.conflictCount).rjust(3), ('%.2f' %(c.priority)).rjust(6), '', c.name.ljust(32), repr(c.i).rjust(2), '', c.previousCourse.name)

#People
# with open(inputCSV, 'r') as csvfile:
# 	rosters = csv.reader(csvfile)
# 	for row in rosters:
# 		print(', '.join(row))
# print()                
# for p in Students:
# 	print(p.name + ' Group: ' + p.pType)
# for p in Teachers:
# 	print(p.name + ' Status: ' + p.pType)
# for p in Rooms:
# 	print(p.name + p.pType)
##################################################

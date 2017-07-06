from modules.Schedule_FilePaths import *
from modules.Schedule_Classes import *
#from modules.Input_CoursesPeople import *
#from modules.Input_Rosters import *
from Import_Rosters import *
from modules.Schedule_Functions import *

#Set file type
fileType = 'Master'      #CSV output with all posibilities.
#fileType = 'Formatted'  #Schedule & StudyHall of first solution found.


#Output files
g = open(solutionsCSV, 'w')
g.write(",".join(str(cl.name) for cl in CourseList))
g.write("\n")
g.close()


foo = MasterAssign(0,1,fileType)
while foo == False:
	foo = Continue(fileType,0)
if foo != True:
	print("Error unexpected value for foo.")
	eL = open(ErrorLog, 'w')
	eL.write("Error unexpected value for foo.\n")
	eL.write(foo)
	eL.close()
import os

##################################################################################
folder = os.getcwd() + '\\Output\\'
#Create output folder if it doesn't exist.
if not os.path.exists(folder):
	os.makedirs(folder)

#Input Files
inputCSV = os.getcwd() + '\\input.csv'

#Output files
solutionsCSV = folder + 'Solutions.csv'

solution     = folder + 'Solution.txt'
studyHall    = folder + 'StudyHall.txt'
MSstudyHall  = folder + 'MS StudyHall.txt'
HSstudyHall  = folder + 'HS StudyHall.txt'

basic        = folder + 'Basic Info.txt'

ErrorLog     = folder + 'Error Log.txt'
##################################################################################
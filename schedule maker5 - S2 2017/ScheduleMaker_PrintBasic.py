from modules.Schedule_FilePaths import *
from modules.Schedule_Classes import *
#from modules.Input_CoursesPeople import *
#from modules.Input_Rosters import *
from Import_Rosters import *
from modules.Schedule_Functions import *

#Run this only once.
Constructor()

f = open(basic, 'w')

for c in CourseList:
	f.write("{0}\n".format(c.name))
f.write("\n")

for c in CourseList:
	f.write("{0}\n".format(c.name))
	for p in c.people:
		f.write("{0}\n".format(p.name))
	f.write("\n")

for s in Students:
	f.write("{0}\n".format(s.name))
	for q in s.schedule:
		f.write("{0}\n".format(q.name))
	f.write("\n")
for t in Teachers:
	f.write("{0}\n".format(t.name))
	for q in t.schedule:
		f.write("{0}\n".format(q.name))
	f.write("\n")

f.close()

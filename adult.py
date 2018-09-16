 # If age is given person adult or not
""" pdb is python debugger used below as module
 pdb.set_trace() is used from the line where you want to start the debug
"""
import pdb
#pdb.set_trace()

try:
    age = int(raw_input("Enter the age:"))
    if age <= 10:
        print 'Person is minor'
		
    elif age ==18:
	    print ' Person can buy cigarette and chew pan'
    elif age >=10:
	    print ' Person can chew pan'
    elif age > 25:
	    print 'Person can smoke,chew pan and have gf like chandru'
		
except:
    print'ValueError: invalid literal for int(): Age should be integer value'
	
#pdb.set_trace()

 
    
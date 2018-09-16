import pdb
try:
    #pdb.set_trace()
    count=-1
    openfile=open("dict.txt","r")
    filecontent=openfile.readlines()
    for i in filecontent:
        count=count+1
    print count
    #print filecontent
       
    openfile.close()
except:
    print "error"	
	


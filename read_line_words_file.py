import pdb
f=open("dict.txt","r")
readline = f.readlines()
#readword = f.readword()
#readchar = f.read()

# uncomment below for loop and comment other for loops for Read file and print lineswise

#for i in readline:
   # print i
   #print "******************"
   #f.close()
# uncomment below for loop and comment other for loops for Read file and print char	wise
#for i in readchar:
    #print i
	#f.close()
# uncomment below for loop and comment other for loops for Read file and print word wise	
for i in readline:
    print(i.split(' ',))
    print "\n"
    f.close()
    


	

import pdb
searchword=raw_input("Enter the string to search in dict.txt file:")
f=open("dict.txt","r")
readline=f.readlines() # use this for line comparison
readword=f.read() # use this for word comparison
#for i in readline:
if(searchword in readline):
    print ("word found")
else:
    print ("word not found")
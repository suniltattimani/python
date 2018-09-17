import pdb
import linecache
#pdb.set_trace()
f=open("dict.txt", "r")
readline=f.readlines()
f.close()
print readline[4].upper()
print readline[9].upper()
# below for loop prints 5th character from each line/list
#for i in readline:
 #   print i[5]
#Use below module print one specific line from a file
#line=linecache.getline("dict.txt", 5)

# Below logic prints odd and even lines separately from a file
index=0
even =list()
odd= list()
for i in readline:
    if index%2 !=0:
	    even.append(i)
    else:
        odd.append(i)
    index += 1
evenline = "".join(even)
print("********************Even lines of file*************************")
oddline = "".join(odd)
print(evenline)
print("********************Odd lines of file*************************")
print(oddline)


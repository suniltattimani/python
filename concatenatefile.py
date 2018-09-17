import pdb
#pdb.set_trace()
f=open("dict.txt","r")
f2=open("dict.txt","w")
f1=open("sunil.txt","r")
fread=f.readlines()
#f2write=f2.writelines()
f1read=f.readlines()
f.close()
f1.close()
f2.close()
for i in f1read:
    combine= (f2.writelines().append(i))
    print combine
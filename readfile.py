with open ("dict.txt", "r") as f:
    filecontent = f.readlines()
	
print  'file content is %s ' % type((filecontent))

for file in filecontent:
   print  file.upper()
   print '============='
   
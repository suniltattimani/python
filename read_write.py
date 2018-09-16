try:
    with open ("dict.txt", "r") as f:
        with open("sunil.txt", "w") as f1:
	        for line in f:
		        filecontent=f1.writelines(line.upper())
except:			
pass
print filecontent
			

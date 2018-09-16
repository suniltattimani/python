print 'a-> add'
print 'b-> sub'
print 'c-> mul'
print 'd-> div'

choice = raw_input('Enter your choice: ')
num1 = raw_input('Enter num1: ')
num2 = raw_input('Enter num2: ')
#add = int(num1)+int(num2)
sub = int(num1)-int(num2)
mul = int(num1)*int(num2)
div = int(num1)/int(num2)

if choice == "a":
   # print "%d" %(add)
    print int(num1)+int(num2)
	
	
if choice == "b":
    print "%d" %(sub)

if choice == "c":
    print "%d" %(mul)
	
if choice == "d":
    print "%d" %(div)
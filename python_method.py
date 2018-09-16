""" This program is written to practice the python methods"""

def add_numbers(a, b):
    return a+b
print "addition of two numbers is %d" %(add_numbers(30,9))

def substract ( a, b):
    return a-b
	
print substract (44, 8)

def test():
    pass

def multiply (b, c, d):
    return c*b*d
	
print multiply (4, 7, 2)

def divide (a,b):
    result = 0
    try:
        result = a/b
    except ZeroDivisionError:
	    print 'exception occured'
    return result

print divide(4, 0)
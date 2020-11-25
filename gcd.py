def computeGCD(x, y): 
    while(y): 
	    x, y = y, x % y 
    return x

if __name__ == "__main__":
    a = int(input("Enter the first number:"))
    m = int(input("Enter the second number:"))
    b = computeGCD(a,m)
    print("The greatest common divisor of "+str(a)+" and "+str(m)+" is "+str(b))


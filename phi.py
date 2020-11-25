def computeGCD(x, y): 
    while(y): 
	    x, y = y, x % y 
    return x


def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (computeGCD(i, n) == 1): 
            result+=1
    return result

if __name__ == "__main__":
    n = int(input("Enter the number:"))
    print("The Euler's Totient Function for "+str(n)+" is "+str(phi(n)))

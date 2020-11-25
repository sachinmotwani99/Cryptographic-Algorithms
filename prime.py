def isprime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 
        
if __name__ == "__main__":
    n = int(input("Enter the number:"))
    if(isprime(n)):
        print("Given Number is a prime number")
    else:
        print("Given number is not a prime number")
    

def factorisation(n):
    l = []
    while(n%2 == 0):
        l.append(2)
        n = n/2
    for i in range(2,int(n)):
        while(n%i ==0):
            l.append(i)
            n=n/i
    if(n>2):
        l.append(int(n))
    return l



if __name__ == "__main__":
    a = int(input("Enter the number to find its prime factorization:"))
    b = factorisation(a)
    print("The prime factorization of "+str(a)+" is: ")
    s = str(b[0])
    n = len(b)
    for i in range(1,n):
        s = s+" X "+str(b[i])
    print(s)
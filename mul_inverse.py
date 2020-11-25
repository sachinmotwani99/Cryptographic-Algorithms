def m_inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i

if __name__ == "__main__":
    a = int(input("Enter the value of a:"))
    m = int(input("Enter the value of m:"))
    b = m_inv(a,m)
    print("The multiplicative inverse of "+str(a)+" in modulo "+str(m)+" is "+str(b))


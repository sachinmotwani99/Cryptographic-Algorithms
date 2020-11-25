def m_inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i

def crt(num, rem, k) : 
      
    prod = 1
    for i in range(0, k) : 
        prod = prod * num[i] 
  
    result = 0
  
    for i in range(0,k): 
        pp = prod // num[i] 
        result = result + rem[i] * m_inv(pp, num[i]) * pp 
      
      
    return result % prod 
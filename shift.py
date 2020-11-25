
#---------Shift Cipher-----------
def ShiftEncrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result


def ShiftDecrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) - s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) - s - 97) % 26 + 97) 
  
    return result


if __name__ == "__main__":
    n = input("Enter the string to encrypt:")
    key = int(input("Enter the key value(0-25):"))
    st = ShiftEncrypt(n,key)
    print("Encrypted Text: "+st)
#-------latin alphabet cipher
def latinalpha(str):
    l = []
    for i in range(len(str)):
        if str[i] >= "A" and str[i] <= "Z":
            x=ord(str[i])-ord("A")+1
            l.append(x)
        if str[i] >= "a" and str[i] <= "z":
            x=ord(str[i])-ord("a")+1
            l.append(x)
    return l

if __name__ == "__main__":
    s = input("Enter the plaintext:")
    print("The encrypted text is:")
    print(latinalpha(s))


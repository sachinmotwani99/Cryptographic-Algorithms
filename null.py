
##--------null cipher
def decode(string): 
	
	res = "" 

	found = False

	for charcter in string: 

		if charcter == ' ': 
			found = False
			continue

		if not found: 
			if charcter>='A' and charcter<='Z' or charcter>='a' and charcter<='z': 
				res += charcter 
				found = True

	return res.lower() 

if __name__ == "__main__":
    n = input("Enter the string to encrypt:")
    st=decode(n)
    print("Encrypted Text: "+st)


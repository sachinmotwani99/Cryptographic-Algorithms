
PT = input("Enter the text you want to encrypt : ").strip().upper()
plainText = list(PT)

k = input("Enter the key : ").strip().upper()
key = list(k)
print("Plaintext = ",PT)
print("Key = ",k)


def PlaintextPreprocessing(plainText):
    #Remove spaces between the plaintext
    #List plaintext[] is used to merge the words in the sequence (i.e. plaintext) to handle spaces between the words
    plaintext = []
    for p in plainText :
        if p!=" ":
            plaintext += p
        else:
            continue 

        #Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the matrix as we need only 25 alphabets instead of 26. If the plaintext contains J, then it is replaced by I
        if p=='J':
            ind = plaintext.index(p)
            plaintext[ind] = 'I'

    for p in plaintext :
        #check of length of plaintext is odd, then append X at the end
        x="X"
        if len(plaintext)%2!=0:
            plaintext += x
    return plaintext 



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#call
plaintext = PlaintextPreprocessing(plainText) 

#---------------------------------------
pair_of_plaintext = []
def Make_Pair_PT(plaintext):
    #make alphabet pair of plaintext and store it in pair_of_plaintext[] list
    for pp in range(0,len(plaintext),2):
        pair_of_plaintext.append(plaintext[pp:pp+2])

    #If a pair is a repeated letter, insert filler like X
    for pair in range(0,len(pair_of_plaintext)):
        if pair_of_plaintext[pair][0] == pair_of_plaintext[pair][1]:
            pair_of_plaintext[pair][1] = 'X'

    print(pair_of_plaintext)
    return pair_of_plaintext 

#call
print("Plaintext is divided into pairs, which are :--->")
Make_Pair_PT(plaintext)
#++++++++±+++++++++++++++++++++++++++++++-

ALPH = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ALPH_len = len(ALPH)


#@@@@@@ (To generate Playfair Matrix)@@@@@@
def Playfair_Matrix(ALPH,ALPH_len):
    #This is used to keep track of the key alphabet remaining
    key_len = len(key)

    #index ind_ALPHA to keep track of the alphabet in the ALPH list
    ind_ALPHA = 0

    #This is used to pop those elements in ALPH list as these alphabet is in the key list (which is already taken in the Playfair_matrix )
    for k in key:
        for a in ALPH:
            if k==a:
                ALPH_index = ALPH.index(a)
                ALPH.pop(ALPH_index)


    #It is a 5X5 matrix, containing the alphabets in some order like ---firstly key is placed in it then remaining alphabet is placed in the same order as they appear (NOTE---If the alphabet which is in key, that alphabet is not placed in the remaining block.)
    #(NOTE---Preference of I/J is same and kept in the same block)
    playfair_matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    ind=0

    #Built playfair_matrix for different key you entered
    for i in range(0,5):
        for j in range(0,5):
            if key_len != 0:
                #This will place all the alphabets in the key
                playfair_matrix[i][j]=key[ind]
                ind += 1
                key_len -=1
            else:
                #Fill remaining entries in the playfair_matrix i.e. place remaining alphabet to playfair_matrix list from ALPH list
                if ALPH_len !=0:
                    playfair_matrix[i][j] = ALPH[ind_ALPHA]
                    ALPH_len -= 1
                    ind_ALPHA +=1
                
     
    return playfair_matrix   
      
      
#call
playfair_matrix = Playfair_Matrix(ALPH,ALPH_len)   
print("Playfair Matrix 5X5 is ---->")  
print(playfair_matrix) 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#+++++++++++ Type 1:- Rectangle or square shape (means a block)++++++++++++++++

#Locate the first alphabet of the pair in playfair_matrix[] and find the row where tye other alphabet of the pair lies such that we get the rectangle or square shape block

def Type1(loc_first_alpha_1i,loc_first_alpha_1j,loc_second_alpha_2i,loc_second_alpha_2j):
    for i in range(0,len(pair_of_plaintext)):
        cipher_pair = playfair_matrix[loc_first_alpha_1i][loc_second_alpha_2j]
        cipher_pair = cipher_pair + playfair_matrix[loc_second_alpha_2i][loc_first_alpha_1j]
    
    print(cipher_pair) 
    return cipher_pair  


#@@@@@@@@@Type2:--Alphabets in pair are in same row
def Type2(loc_first_alpha_1i,loc_first_alpha_1j,loc_second_alpha_2i,loc_second_alpha_2j):
    for i in range(0,len(pair_of_plaintext)):
        #check first alphabet of the pair is at the extreme end
        if loc_first_alpha_1j ==4:
            cipher_pair = playfair_matrix[loc_first_alpha_1i][0]
            cipher_pair = cipher_pair + playfair_matrix[loc_first_alpha_1i][loc_second_alpha_2j+1]

        #check second alphabet of the pair is at the extreme end
        if loc_second_alpha_2j ==4:
            cipher_pair = playfair_matrix[loc_first_alpha_1i][loc_first_alpha_1j+1]
            cipher_pair = cipher_pair + playfair_matrix[loc_first_alpha_1i][0]

        #If first or second alphabet of the pair are not at the extreme end
        if (loc_first_alpha_1j!=4) and (loc_second_alpha_2j!=4):
            cipher_pair = playfair_matrix[loc_first_alpha_1i][loc_first_alpha_1j+1]
            cipher_pair = cipher_pair + playfair_matrix[loc_second_alpha_2i][loc_second_alpha_2j+1]
    print(cipher_pair)
    return cipher_pair 


#++++++++++++(Type3 :-- Alphabets in pair are in same col)+++++++++++++++++++++++++
def Type3(loc_first_alpha_1i,loc_first_alpha_1j,loc_second_alpha_2i,loc_second_alpha_2j):
    for i in range(0,len(pair_of_plaintext)):
        #since both alphabets of the pair are in same col, so either first alphabet or second alphabet lies at the bottom extreme, but not both simultaneousy

        #check first alphabet of the pair is at the bottom extreme end
        if loc_first_alpha_1i ==4:
            cipher_pair = playfair_matrix[0][loc_first_alpha_1j]
            cipher_pair = cipher_pair + playfair_matrix[loc_second_alpha_2i+1][loc_second_alpha_2j]

        if loc_second_alpha_2i ==4:
            cipher_pair = playfair_matrix[loc_first_alpha_1i+1][loc_first_alpha_1j]
            cipher_pair = cipher_pair + playfair_matrix[0][loc_second_alpha_2j]

        #If first or second alphabet of the pair are not at the bottom extreme end
        if (loc_first_alpha_1i!=4) and (loc_second_alpha_2i!=4):
            cipher_pair = playfair_matrix[loc_first_alpha_1i+1][loc_first_alpha_1j]
            cipher_pair = cipher_pair + playfair_matrix[loc_second_alpha_2i+1][loc_second_alpha_2j]

    print(cipher_pair)
    return cipher_pair 


#++++++++++++++(Encryption)++++++++++++++++
cipher_pair = []
#combine each pair of ciphertext returned into cipher_text_final[] list
cipher_text_final = []

def Encryption(playfair_matrix, pair_of_plaintext,cipher_pair):
    #search each pair alphabet of plaintext in playfair_matrix[] and observe the location of the pair alphabet
    print("Encrypted Ciphertext is --->")
    for pp in pair_of_plaintext :
        for i in range(0,5):
            for j in range(0,5):
                #The below two if statement is for use when in a pair (in plaintext) of alphabet is in different row and col
                if pp[0]==playfair_matrix[i][j]:
                    loc_first_alpha_1i = i
                    loc_first_alpha_1j = j
                if pp[1] == playfair_matrix[i][j]:
                    loc_second_alpha_2i = i
                    loc_second_alpha_2j = j
        

        #if both alphabets of pair are in different row and col
        if (loc_first_alpha_1i!=loc_second_alpha_2i) and (loc_first_alpha_1j!= loc_second_alpha_2j):
           print("{}---->".format(pp),end=" ")
           cipher_Type1 =Type1(loc_first_alpha_1i, loc_first_alpha_1j, loc_second_alpha_2i, loc_second_alpha_2j)
           cipher_text_final.append(cipher_Type1)
           
           
 
        #pair (in plaintext) of alphabets is in same row
        if loc_first_alpha_1i == loc_second_alpha_2i:
            print("{}---->".format(pp), end =" ") 
            cipher_Type2 = Type2(loc_first_alpha_1i, loc_first_alpha_1j, loc_second_alpha_2i, loc_second_alpha_2j)
            cipher_text_final.append(cipher_Type2)

        #pair (in plaintext) of alphabets is in same col
        if loc_first_alpha_1j == loc_second_alpha_2j:
            print("{}---->".format(pp), end=" ")
            cipher_Type3 = Type3(loc_first_alpha_1i, loc_first_alpha_1j, loc_second_alpha_2i, loc_second_alpha_2j)
            cipher_text_final.append(cipher_Type3)


#call
Encryption(playfair_matrix, pair_of_plaintext, cipher_pair)

#print combined pair if Ciphertext 
print("Ciphertext is --->")

for c in cipher_text_final :
    print("".join(c), end="")
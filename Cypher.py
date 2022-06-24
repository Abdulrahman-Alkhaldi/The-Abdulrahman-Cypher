#abdulrahman alkhaldi 
# 2191114843
Cypher = 'Abdulrahman'
# creating a list of the alphabetical order of each chr in my name
Cypher_lst = [ord(i.lower()) - 96 for i in Cypher]
# [1, 2, 4, 21, 12, 18, 1, 8, 13, 1, 14]


def encrypt(string):
    StringList = []
    count = 0
    for i in string:
        # looping through the string using %
        StringList.append((ord(i.lower())-96) +
                        Cypher_lst[count % len(Cypher)] ) # encrypting the string
        count+=1
    
    EncryptedString = ''
    for i in StringList:
        EncryptedString += chr(i+96) # adding 96 to get the integer representation of the character
    return  EncryptedString

def decrypt(string):
    StringList = []
    count = 0
    for i in string:
        # looping through the string using modulus
        StringList.append((ord(i.lower())-96) -
                        Cypher_lst[count % len(Cypher)] ) # decrypting the string
        count += 1

    DecryptedString = ''
    for i in StringList:
        DecryptedString += chr(i+96) # adding 96 to get the integer representation of the character
    return DecryptedString


# write a python program to translate into a secret code language. Use the rules below to translate normal english to a secret code language.
        # Encoding:
            # if: the word consist atleast 3 characters, remove the first letter and append it at the end.
            # now append the three random character at the starting and at the end.
            # else: simply reverse the string.
        #Decoding: 
            # if: the word contains less than 3 characters, reverse it.
            # else: remove 3 random character from the start and the end, now remove the last letter and append it at the beginning 
        # your program should ask where you want to code or decode. 
import random
# FUNCTION to switch the first character of the string to the end.
def swappingFront_toBack(strings):
    if len(strings) == 0 or len(strings) == 1:
        return strings
    return strings[1:] + strings[0]
# FUNCTION to switch the end character of the string to the beginning.
def swappingBack_toFront(string):
    if len(string) == 0 or len(string) == 1:
        return string
    return string[len(string)-1] + string[0:len(string)-1]
# GENERATING random characters... 
def genRandom():
    selectRandom = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(3))
    return selectRandom
# ENCODING the secret code...
def encoding(userInput):
    split = userInput.split(" ")
    for i in range(len(split)):
        if(len(split[i]) == 2):
            split[i] = swappingFront_toBack(split[i])
        elif(len(split[i]) > 2):
            split[i] = swappingFront_toBack(split[i])
            ran1 = genRandom()
            ran2 = genRandom()
            split[i] = ran1 + split[i] + ran2
            split[i].strip()
        else:
            split[i] = swappingFront_toBack[split[i]]
    str = ' '
    return str.join(split)
#DECODING the secret code...
def decoding(encodedOutput):
    split = encodedOutput.split(" ")
    for i in range(len(split)):
        if(len(split[i]) == 2):
            split[i] = swappingBack_toFront(split[i])
        elif(len(split[i]) > 2):
            split[i] = split[i].replace(split[i][0:3],"")
            split[i] = split[i].replace(split[i][len(split[i])-3:len(split[i])],"")
            split[i] = swappingBack_toFront(split[i])
        else:
            split[i] = swappingBack_toFront(split[i])
    str = ' '
    return str.join(split)
usersInput = input("Enter your Message : ")
encodingOption = input("To Encode your Message Enter `YES` or else `NO` : ")
if encodingOption == "YES":
    encodingOutput = encoding(usersInput)
    print("Encoded Message : ",encodingOutput)
    decodingOption = input("To Decode the Message Enter `YES` or else `NO` : ")
    if decodingOption == "YES":
        decodingOutput = decoding(encodingOutput)
        print("Decoded Message",decodingOutput)
    else:
        print("Encoded Meassage",encodingOutput)
else:
    print(usersInput)

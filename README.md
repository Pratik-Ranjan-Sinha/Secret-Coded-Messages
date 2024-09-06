The problem was to:

write a python program to translate into a secret code language. Use the rules below to translate normal english to a secret code language.

        # Encoding:
            # if: the word consist atleast 3 characters, remove the first letter and append it at the end.
            # now append the three random character at the starting and at the end.
            # else: simply reverse the string.
        #Decoding: 
            # if: the word contains less than 3 characters, reverse it.
            # else: remove 3 random character from the start and the end, now remove the last letter and append it at the beginning 


Where the OUTPUT was : 

    Enter your Message : HEllo My name is pratik ranjan sinha
    
    To Encode your Message Enter `YES` or else `NO` : YES
    
    Encoded Message :  LVbElloHvPp yM sBOamenRWc si DzJratikpAcX qFAanjanrtvK bAUinhasGNd
    
    To Decode the Message Enter `YES` or else `NO` : YES
    
    Decoded Message HEllo My name is pratik ranjan sinha

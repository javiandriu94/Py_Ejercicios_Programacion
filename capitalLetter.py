def capitalLetter(s):
    string = ""
    for i in range(len(s)):
        if(i == 0 ):
            string += s[i].upper()
        elif (s[i].isalpha() and  s[i-1] == " "):
            string += s[i].upper()
        else:
            string += s[i].lower()
            
    return string
print(capitalLetter("javier vasquez"))

            
def isPalindrome(text):
    text2 = ''.join([char.lower() for char in text if char.isalpha()])
    
    reverse = ''
    for i in range(len(text2) - 1, -1, -1):
        reverse += text2[i]
    
    if text2 == reverse:
        print("Is palindrome")
    else:
        print("It is not palindrome")
       
    
   
    
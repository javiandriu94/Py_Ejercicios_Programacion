#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(text):
    swap=''
    for char in text:
        if(char.islower()):
            swap += char.upper()
        else:
            swap += char.lower()
    return swap

print(swap_case('HolaHHAHAHAHooooo'))
def removeVowelInAString (text):
    text2 = [char.lower() for char in text if char.isalpha() and char not in "aeiou"]
    return text2

print(removeVowelInAString("jaahuahsadjkahkjdasa"))
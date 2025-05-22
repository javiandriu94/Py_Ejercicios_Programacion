def vowelConsonantCounter(text):
    text2 = [char.lower()  for char in text if char.isalpha()]
    vowel=0
    consonant=0
    for i in text2:
        if i in 'aeiou':
            vowel +=1
        else:
            consonant += 1   
    return (vowel, consonant)

texto = "HolaMundo! EstoEsCamelCase123 :)"
print(vowelConsonantCounter(texto))


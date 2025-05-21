def vowelConsonantCounter(text):
    vowel=0
    consonant=0
    for i in text:
        if text.isalpha():
            if i in 'aeiou':
                vowel +=1
            else:
                consonant += 1
    return (vowel, consonant)

texto = "HolaMundo! EstoEsCamelCase123 :)"
print(vowelConsonantCounter(texto))


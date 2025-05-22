def counterNumberInAString (text):
    counter = len([char for char in text if char.isdigit()])
    return counter
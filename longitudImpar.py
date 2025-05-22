def oddLenWord (words):
    oddLen = [word for word in words if len(word) % 2 != 0]
    return oddLen
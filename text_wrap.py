def text_wrap(string, max_width):
    lines = ""
    for i in range(len(string)):
        lines +=  string[i]
        if ((i+1) % max_width == 0):
            lines += "\n"
    return lines

print(text_wrap("HAHASKKSAKSKALDJKSDKSJD", 3))

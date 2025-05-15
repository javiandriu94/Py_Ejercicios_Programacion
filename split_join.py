def split_and_join(line):
    for char in line:
        if(char == ' '):
            result = line.split(" ")
            result = "-".join(result)
    return result

print(split_and_join("this is a string"))

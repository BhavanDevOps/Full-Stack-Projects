def convert(word):
    first = True
    for char in word:
        if first:
            result = char.lower()
        elif char.isupper():
            result+= '_' + char.lower()
        else:
            result+= char
        first = False
    return result

word = input().strip()
snake = convert(word)
print(snake)
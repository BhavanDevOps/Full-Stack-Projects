given_word=input()

for char in given_word:
    if char.upper()==char:
        if not char.isdigit():
            print(char)
            break
text = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newtext = ""
textlen = len(text)

for i in range(textlen):
    if text[i] not in vowels:
        newtext = newtext + text[i]


text = newtext
print(text)
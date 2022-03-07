word = ''
for ch in input():
    word += ch.lower()
reversed_word = word[::-1]
print(word == reversed_word)
word=input()

modified_word=""
for character in word:
    uppercase_char=character.upper()
    if uppercase_char==character:
        modified_word=modified_word+character.lower()
    else:
        modified_word=modified_word+character.upper()
        
print(modified_word)
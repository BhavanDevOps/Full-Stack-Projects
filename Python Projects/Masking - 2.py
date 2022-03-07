word=input()
first_character=word[0:2]
word_len=len(word)
second_character=word[word_len-2:]
num_star="*"*(word_len-4)
result=first_character+num_star+second_character
print(result)
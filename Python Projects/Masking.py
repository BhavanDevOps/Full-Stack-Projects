word=input()
first_character=word[0]
word_len=len(word)
second_character=word[word_len-1]
num_star="*"*(word_len-2)
result=first_character+num_star+second_character
print(result)
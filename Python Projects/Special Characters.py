given_sentence=input()
length=len(given_sentence)
given_sentence=given_sentence.lower()
vowel_count=0
consonants_count=0

for i in range(0,length):
    if given_sentence[i] in ["a","e","i","o","u"]:
        vowel_count+=1
    elif (given_sentence[i]>="a") and(given_sentence[i]<="z"):
        consonants_count+=1
        
print(vowel_count)
print(consonants_count)
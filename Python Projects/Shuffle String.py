s=input()
len_s=len(s)
shuffled_s=""
for i in range(len_s):
    index=int(input())
    shuffled_s=shuffled_s+s[index]
print(shuffled_s)
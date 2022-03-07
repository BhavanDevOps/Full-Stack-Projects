num=int(input())

term_num="2"
total=0
for i in range(1,num+1):
    term=term_num*i
    total+=int(term)
print(total)
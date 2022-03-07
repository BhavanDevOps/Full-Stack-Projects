n=int(input())

for i in range(1,n+1):
    stars="* "*i
    middle_spaces="  "*(2*(n-i))
    print(stars+middle_spaces+stars)
    
for i in range(n):
    stars="* "*(n-i)
    middle_spaces="  "*(2*i)
    print(stars+middle_spaces+stars)
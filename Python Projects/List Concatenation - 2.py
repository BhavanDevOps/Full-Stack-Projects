n = int(input())
list_a=[]
for i in range(n):
    value=input()
    list_a+=[value]
    
new_list=list_a[ :3]+list_a[n-3:]
print(new_list)
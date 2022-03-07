num_list=input().split()


new_list=[]
for item in num_list:
    n=int(item)
    new_list.append(n)
    
    
num_set=set(new_list)
num_list=list(num_set)
num_list.sort()
print(num_list)

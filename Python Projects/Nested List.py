def convert_string_to_int(list_a):
    new_list=[]
    for item in list_a:
        num=int(item)
        new_list.append(num)
    return new_list

n=int(input())
num_list=[]

for i in range(n):
    list_a=input().split()
    list_a=convert_string_to_int(list_a)
    num_list.append(list_a)
    
print(num_list)
    
def convert_string_to_int(list_a):
    new_list=[]
    for item in list_a:
        num=int(item)
        new_list.append(num)
    return new_list
    
    
num_list=[]
for i in range(3):
    values_llist=input().split()
    values_llist=convert_string_to_int(values_llist)
    values_set=set(values_set)
    num_list,append(values_set)
    
    
intersection_a=num_list[0].intersection(num_list[1])
intersection_b=intersection_a.intersection(num_list[2])

result=list(intersection_b)
result.sort()

print(result)
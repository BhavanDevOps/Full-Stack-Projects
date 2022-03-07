n=int(input())
num_list=[]
zero_index_list=[]
first_index_list=[]

for i in range(n):
    values_list=input().split()
    first_value=int(values_list[0])
    zero_index_list.append(first_value)
    second_value=int(values_list[1])
    first_index_list.append(second_value)
    
zero_index_min_max_tuple=(max(zero_index_list),min(zero_index_list))
first_index_min_max_tuple=(max(first_index_list),min(first_index_list))

print(zero_index_min_max_tuple)
print(first_index_min_max_tuple)
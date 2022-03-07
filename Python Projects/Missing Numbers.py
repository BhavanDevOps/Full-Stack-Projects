def convert_string_to_int(list_a):
    new_list=[]
    for item in list_a:
        num=int(item)
        new_list.append(num)
    return new_list
    
num_list=input().split()
num_list=convert_string_to_int(num_list)
maximum=max(num_list)
num_set=set(num_list)

first_n_num_set=set(range(1,maximum+1))
missing_num_set=first_n_num_set.difference(num_set)
missing_num_set=list(missing_num_set)
missing_num_set.sort()
print(missing_num_set)
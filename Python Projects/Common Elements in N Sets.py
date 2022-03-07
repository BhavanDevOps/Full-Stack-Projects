def convert_string_to_int(list_a):
    new_list=[]
    for item in list_a:
        num=int(item)
        new_list.append(num)
    return new_list
    
def get_intersection_of_n_sets(num_set_list):
    result=num_set_list[0]
    for num_set in num_set_list:
        result=result.intersection(num_set)
    return result
    
n=int(input())
num_set_list=[]
for i in range(n):
    values_list=input().split()
    values_list=convert_string_to_int(values_list)
    values_set=set(values_list)
    num_set_list.append(values_set)
    
result_set=get_intersection_of_n_sets(num_set_list)
result_list=list(result_set)
result_list.sort()
print(result_list)
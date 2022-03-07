def converting_string(num_list):
    new_list=[]
    for item in num_list:
        num=int(item)
        new_list.append(num)
        return new_list



List_a=input().split(",")
list_b=input().split(",")

List_a=converting_string(List_a)
list_b=converting_string(list_b)

set_a=set(List_a)
set_b=set(list_b)

result_set=set_a.intersection(set_b)
result_list=list(result_set)
result_list.sort()
print(result_list)
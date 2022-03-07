def convert_nested_list_to_list_of_tuples(nested_list):
    # Complete this function
    tuples_list=[]
    for each_list in nested_list:
        tuple_a=tuple(each_list)
        tuples_list.append(tuple_a)
    return tuples_list


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


n = int(input())
num_list = []

for i in range(n):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)


tuples_list = convert_nested_list_to_list_of_tuples(num_list)
print(tuples_list)

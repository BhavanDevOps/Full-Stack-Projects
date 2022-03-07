def convert_string_to_int(list_a):
    new_list=[]
    for item in list_a:
        num=int(item)
        new_list.append(num)
    return new_list
    
num_list=input().split()
num_list=convert_string_to_int(num_list)

num_set=set(num_list)
if len(num_set)==1:
    print("True")
else:
    num_list=list(num_set)
    num_list.sort()
    print(num_list)
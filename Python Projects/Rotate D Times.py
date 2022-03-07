def convert_string_to_int(str_num_list):
    new_list=[]
    for item in str_num_list:
        num=int(item)
        new_list.append(num)
    return new_list
    
    
str_num_list=input().split(",")
rotate_times=int(input())


int_list=convert_string_to_int(str_num_list)
len_of_list=len(int_list)
val=rotate_times%len_of_list

first_part=int_list[0:val]
second_part=int_list[val:]
second_part.extend(first_part)
print(second_part)
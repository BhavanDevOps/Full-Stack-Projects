list_a=input().split(",")

num_list=[]
for item in list_a:
    is_digit=item.isdigit()
    if is_digit:
        number=int(item)
        num_list.append(number)
        
print(num_list)
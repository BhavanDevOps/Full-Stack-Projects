given_string=input()
number_list=given_string.split(",")

length_of_number_list=len(number_list)


for i in range(length_of_number_list):
    number_list[i]=int(number_list[i])
    
    
number_list=sorted(number_list)
largest_number=max(number_list)
smallest_number=min(number_list)
difference=largest_number-smallest_number
print(difference)
given_string=input()
k=int(input())

number_list=given_string.split(",")
length_of_number_list=len(number_list)

for i in range(length_of_number_list):
    number_list[i]=int(number_list[i])
    
    
number_list=sorted(number_list)
largest_number=number_list[-k]
print(largest_number)
given_string=input()
list_string=given_string.split(",")
length_of_list_string=len(list_string)



for i in range(length_of_list_string):
    list_string[i]=int(list_string[i])
    
    
list_string=sorted(list_string)

print(list_string)
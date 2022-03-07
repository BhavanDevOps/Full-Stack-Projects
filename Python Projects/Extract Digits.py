str_1=input()

digits_list=[]

for char in str_1:
    if char.isdigit():
        digits_list+=[int(char)]
    
        
sum_of_numbers=sum(digits_list)
print(sum_of_numbers)
min_of_numbers=min(digits_list)
print(min_of_numbers)
max_of_numbers=max(digits_list)
print(max_of_numbers)

num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
n=int(input())
new_list=[]
for number in num_list:
    if number > n:
        new_list+=[number]
        
print(new_list)
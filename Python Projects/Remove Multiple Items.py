num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here
list_a=input().split()

for item in list_a:
    num=int(item)
    num_set.discard(num)
    
    
num_list=list(num_set)
num_list.sort()
print(num_list)

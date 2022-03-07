def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Write your code here
row_max=[]
row_min=[]
row_sum=[]
for row in num_list:
    row_max.append(max(row))
    row_min.append(min(row))
    row_sum.append(sum(row))
    
print(max(row_max))
print(min(row_min))
print(sum(row_sum))
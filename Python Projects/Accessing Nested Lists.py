list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here
n=int(input())
new_list=[]

for i in range(n):
    index=input().split()
    tuple_index=int(index[0])
    value_index=int(index[1])
    value=list_a[tuple_index][value_index]
    new_list.append(value)
    
print(new_list)
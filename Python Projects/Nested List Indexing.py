num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
n=int(input())
for tuple_a in num_list:
    is_contain=n in tuple_a
    if is_contain:
        tuple_index=num_list.index(tuple_a)
        n_index=tuple_a.index(n)
        print(str(tuple_index)+" "+str(n_index))
        break
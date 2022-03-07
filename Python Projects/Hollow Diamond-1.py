n=int(input())
#print(n)
left_space_count=n-1
left_space=" "*left_space_count
row_output=left_space+"*"
print(row_output)
hollow_space_count=-1
for row in range(2,n+1):
    left_space_count=n-row
    left_space=" "*left_space_count
    hollow_space_count=hollow_space_count+2
    hollow_space=" "*hollow_space_count
    row_output=left_space+"*"+hollow_space+"*"
    print(row_output)
for row_bottom in range(1,n-1):
    left_space_count=row_bottom
    left_space=" "*left_space_count
    hollow_space_count=hollow_space_count-2
    hollow_space=" "*hollow_space_count
    row_output=left_space+"*"+hollow_space+"*"
    print(row_output)
left_space_count=n-1
left_space=" "*left_space_count
row_output=left_space+"*"
print(row_output)
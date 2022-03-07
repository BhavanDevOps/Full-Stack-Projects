students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
n=int(input())
for i in range(n):
    key_value_pair=input().split()
    key,value=key_value_pair[0],key_value_pair[1]
    students_dict[key]=value
print(students_dict)
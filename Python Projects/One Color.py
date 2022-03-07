given_string=input()
count=0
string_1=given_string.count("R")
string_2=given_string.count("G")

if string_1>string_2:
    count=string_2
else:
    count=string_1
print(count)
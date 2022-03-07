first_number=int(input())
second_number=int(input())
third_number=int(input())


if first_number>second_number:
    greatest_number=first_number
else:
    greatest_number=second_number
    
    
if third_number>greatest_number:
    greatest_number=third_number
print(greatest_number)
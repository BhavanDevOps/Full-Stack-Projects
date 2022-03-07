first_number=int(input())
second_number=int(input())
third_number=int(input())


if first_number<second_number:
    smallest_number=first_number
else:
    smallest_number=second_number
    
    
if third_number<smallest_number:
    smallest_number=third_number
print(smallest_number)
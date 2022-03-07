given_number=int(input())
remainder_2=given_number % 2
remainder_3=given_number % 3
 
 
is_lucky_number=False
if (remainder_2==0) and (remainder_3==0):
    print("Number is divisible by 6")
    is_lucky_number=True
if(remainder_3==0) and( not is_lucky_number):
    print("Number is divisible by 3")
    is_lucky_number=True
if (remainder_2==0) and (not is_lucky_number):
    print("Number is divisible by 2")
    is_lucky_number=True
    
if not is_lucky_number:
    print("Number is not divisible by 2, 3 or 6")
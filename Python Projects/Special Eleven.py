number=int(input())

is_multiple_of_11=((number%11)==0)
is_more_than_11=((number%11)==1)

if is_multiple_of_11 or is_more_than_11:
    print("Special Eleven")
else:
    print("Normal Number")
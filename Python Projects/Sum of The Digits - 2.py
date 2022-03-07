number=input()

is_one_digit=(len(number)==1)
is_two_digit=(len(number)==2)
is_three_digit=(len(number)==3)


if is_one_digit:
    print(number)
elif is_two_digit:
    first_digit=int(number[0])
    second_digit=int(number[1])
    print(first_digit+second_digit)
elif is_three_digit:
     first_digit=int(number[0])
     second_digit=int(number[1])
     third_digit=int(number[2])
     print(first_digit+second_digit+third_digit)
else:
    first_digit=int(number[0])
    second_digit=int(number[1])
    third_digit=int(number[2])
    fourth_digit=int(number[3])
    print(first_digit+second_digit+third_digit+fourth_digit)
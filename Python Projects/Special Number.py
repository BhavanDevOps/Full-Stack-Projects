number=input()
first_input=int(number[0])
second_input=int(number[1])

sum_of_two_digits=(first_input+second_input)
is_sum_equal_to_7=(sum_of_two_digits==7)
is_one_digit_is_7=((first_input==7)or(second_input==7))
is_multiple_of_7=((int(number)%7)==0)


if (is_sum_equal_to_7 or is_one_digit_is_7) or is_multiple_of_7:
    print("Special Number")
else:
    print("Normal Number")
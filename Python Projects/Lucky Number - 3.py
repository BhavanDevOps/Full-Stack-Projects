given_number=int(input())

is_multiple_of_9=(given_number%9==0)

given_number=str(given_number)

first_number=int(given_number[0])
second_number=int(given_number[1])

is_first_number_equal_to_9=(first_number==9)
is_second_number_equal_to_9=(second_number==9)

is_any_digit_equal_to_9=is_first_number_equal_to_9 or is_second_number_equal_to_9

if is_any_digit_equal_to_9 or is_multiple_of_9:
    print("Lucky Number")
else:
    print("Unlucky Number")
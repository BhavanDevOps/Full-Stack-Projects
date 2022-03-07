def fizz_buzz(number):
    # Complete this function
        is_divisible_by_3=(number%3)==0
        is_divisible_by_5=(number%5)==0
        is_divisible_by_both=is_divisible_by_3 and is_divisible_by_5
        
        if is_divisible_by_both:
            msg="FizzBuzz"
        elif is_divisible_by_3:
            msg="Fizz"
        elif is_divisible_by_5:
            msg="Buzz"
        else:
            msg=number
        return msg
        
number = int(input())
# Call the fizz_buzz function
result=fizz_buzz(number)
print(result)
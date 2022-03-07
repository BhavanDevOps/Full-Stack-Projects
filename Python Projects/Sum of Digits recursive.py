def sum_of_the_digits(number):
    # Complete this recursive function
    if number<10:
        return number
    else:
        return(number%10)+sum_of_the_digits(number//10)

number = int(input())
# Call the sum_of_the_digits function
result=sum_of_the_digits(number)
print(result)
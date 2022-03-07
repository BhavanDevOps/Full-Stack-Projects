symbol=input()
first_number=int(input())
second_number=int(input())


if symbol=="+":
    print(first_number+second_number)
elif symbol=="-":
    print(first_number-second_number)
elif symbol=="*":
    print(first_number*second_number)
elif symbol=="/":
    print(first_number/second_number)
else:
    print(first_number%second_number)
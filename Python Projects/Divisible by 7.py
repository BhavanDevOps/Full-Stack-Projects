def divisible_by_seven(arg_1):
    remainder=arg_1%7
    if remainder==0:
        result=True
    else:
        result=False
    print(result)


n = int(input())
divisible_by_seven(n)
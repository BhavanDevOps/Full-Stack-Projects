def show_numbers(number):
    # Complete this Function
    for i in range(number+1):
        if (i%2)==0:
            print(str(i)+" EVEN")
        else:
            print(str(i)+" ODD")

number = int(input())
# Call the show_numbers function
show_numbers(number)

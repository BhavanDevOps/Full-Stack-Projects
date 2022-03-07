first_side=int(input())
second_side=int(input())
third_side=int(input())

condition_1=((first_side + second_side) > third_side)
condition_2=((second_side + third_side) > first_side)
condition_3=((third_side + first_side) > second_side)

if (condition_1 and condition_2) and condition_3:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
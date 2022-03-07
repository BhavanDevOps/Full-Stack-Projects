def get_discount(amount):
    # Complete this function
    if amount<500:
        discount="5%"
    elif (amount>=500) and (amount<2500):
        discount="10%"
    else:
        discount="20%"
    return discount

amount = int(input())
# Call the get_discount function
result=get_discount(amount)
print(result)
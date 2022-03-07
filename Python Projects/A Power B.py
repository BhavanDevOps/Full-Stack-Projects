def calculate_power(x, y):
    # Complete this recursive function
    if y==1:
        return x
    else:
        y-=1
        return x*calculate_power(x,y)

a = int(input())
b = int(input())
# Call the calculate_power function
result=calculate_power(a,b)
print(result)
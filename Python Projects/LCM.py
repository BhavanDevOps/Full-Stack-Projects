m=int(input())
n=int(input())

if m>n:
    greatest_number=m
else:
    greatest_number=n
lcm_found=False
for number in range(greatest_number,(m*n+1)):
    if not lcm_found:
        if ((number%m)==0) and ((number%n)==0):
            lcm_found=True
            lcm=number
print(lcm)
given_integer=int(input())

multiples_of_2=set()
multiples_of_3=set()

for i in range(1,given_integer+1):
    multiples_of_2.add(2*i)
    multiples_of_3.add(3*i)
    
difference=multiples_of_2.difference(multiples_of_3)
symetric_difference=multiples_of_2^(multiples_of_3)

difference=list(difference)
symetric_difference=list(symetric_difference)


difference.sort()
symetric_difference.sort()

print(difference)
print(symetric_difference)
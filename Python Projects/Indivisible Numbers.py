n = int(input())
number = 0
for i in range(1,n+1):
    if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 and i % 9 != 0 and i % 10 != 0:
        number += 1
print(number)
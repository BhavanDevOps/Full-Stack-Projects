a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if int(i ** 0.5) == i ** 0.5:
        count += 1
print(count)
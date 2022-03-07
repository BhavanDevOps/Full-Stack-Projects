n=int(input())

star_line="* "*n
print(star_line)

for row in range(1,n-1):
    hollow_spaces="  "*(n-row-2)
    hollow_line="* "+hollow_spaces+"* "
    print(hollow_line)
print("* ")
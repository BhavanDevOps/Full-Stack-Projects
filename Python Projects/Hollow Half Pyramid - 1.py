n=int(input())

print("* ")
for i in range(n-2):
    hollow_spaces=" "*(2*i)
    hollow_line="* "+hollow_spaces+"* "
    print(hollow_line)
    
star_line="* "*n
print(star_line)
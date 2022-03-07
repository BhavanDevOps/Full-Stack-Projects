n=int(input())

for row in range(0,n):
    stars_count=n-row
    left_star="* "*stars_count
    hollow_spaces="  "*(2*row)
    right_stars="* "*stars_count
    print(left_star+hollow_spaces+right_stars)
    
for row in range(1,n+1):
    stars_count=n-row
    stars="* "*row
    hollow_spaces="  "*(2*stars_count)
    print(stars+hollow_spaces+stars)
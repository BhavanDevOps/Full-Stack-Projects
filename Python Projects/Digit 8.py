n=int(input())

num_of_rows=(2*n)+1
for i in range(1,num_of_rows+1):
    if(i==1) or(i==(n+1)) or(i==num_of_rows):
        print("* "*n)
    else:
        spaces="  "*(n-2)
        print("* "+spaces+"* ")
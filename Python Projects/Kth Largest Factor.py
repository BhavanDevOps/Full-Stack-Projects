number=int(input())
k=int(input())

factor=number
count=0
kth_factor_found=False

for i in range(1,number+1):
    if not kth_factor_found:
        if(number%factor)==0:
            count+=1
        if count==k:
            print(factor)
            kth_factor_found=True
    factor=factor-1
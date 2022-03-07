X=int(input())
sum=0
temp=X
n=len(str(X))
while temp>0:
    d=temp%10
    sum+=d**n
    temp//=10
if X==sum:
    print("True")
else:
    print("False")
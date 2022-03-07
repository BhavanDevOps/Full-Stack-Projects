import string
n=int(input())

for i in range(n):
    slice=string.ascii_uppercase[0:i+1]
    print(" ".join(slice))
   
   

a = int(input())
b = int(input())
c = int(input())
l = [a, b, c]
test = True
for i in l:
    if i >=10 and i <= 20:
        print("True")
        test = False
        break
if test: print("False")
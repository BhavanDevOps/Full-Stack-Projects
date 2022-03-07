list1 = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
input1 = input()
input2 = int(input())
i = input2%7 -1 
if input1 in list1:
    j = list1.index(input1)+i
    if j >= 7:
        j = j - 7
    print(list1[j])
n=int(input())


nums_list=[]

for i in range(n):
    List=input().split()
    if List[0]=='insert':
        index=int(List[1])
        value=int(List[2])
        nums_list.insert(index,value)
    elif List[0]=='append':
        value=int(List[1])
        nums_list.append(value)
    elif List[0]=='pop':
        nums_list.pop()
    elif List[0]=='remove':
        value=int(List[1])
        nums_list.remove(value)
    elif List[0]=='sort':
        nums_list.sort()
    elif List[0]=='print':
        print(nums_list)
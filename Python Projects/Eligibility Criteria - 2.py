M=int(input())
P=int(input())
C=int(input())
MP=M+P
MC=M+C
MPC=M+P+C
if(MP>=100 or MC>=100) and MPC>=180:
    print("True")
else:
    print("False")
    

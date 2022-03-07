M=int(input())
P=int(input())
C=int(input())

MP=M+P
MC=M+C
PC=P+C
MPC=M+P+C
if(M>=60 and P>=50 and C>=45 and MPC>=180)or (MP>=120 or PC>=110):
    print("True")
else:
    print("False")
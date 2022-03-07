M=int(input())
P=int(input())
C=int(input())
MP=M+P
MC=M+C
PC=P+C

if M>=35 and P>=35 and C>=35 and (MP>=90 or MC>=90 or PC>=90):
    print("True")
else:
    print("False")
    

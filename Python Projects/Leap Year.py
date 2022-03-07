def LeapYear(n):
    if(n%4)==0:
        if(n%100)==0:
            if(n%400)==0:
                print("True")
            else:
                print("False")
        else:
            print("True")
    else:
        print("False")
        
        
n=int(input())
LeapYear(n)
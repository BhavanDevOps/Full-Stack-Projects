units=int(input())

bill=0

if units<50:
    bill=2*units
elif units<150:
    bill=(2*50)+ (3*(units-50))
elif units<250:
    bill=(2*50)+(3*100)+(5*(units-150))
elif units>=250:
    bill=(2*50)+(3*100)+(5*100)+(8*(units-250))
    
surcharge=(0.2*bill)

total_bill=(bill+surcharge)

print(total_bill)
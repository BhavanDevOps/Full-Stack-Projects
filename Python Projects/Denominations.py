amount=int(input())

note_100=0
note_50=0
note_10=0
note_1=0

if amount>=100:
    note_100=int(amount/100)
    amount=(amount%100)
if amount>=50:
    note_50=int(amount/50)
    amount=(amount%50)
if amount>=10:
    note_10=int(amount/10)
    amount=(amount%10)
    
note_1=amount

print("100:"+str(note_100))
print("50:"+str(note_50))
print("10:"+str(note_10))
print("1:"+str(note_1))



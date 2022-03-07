given_time=int(input())

morning=((given_time>=4) and (given_time<12))
afternoon=((given_time>=12) and (given_time<16))
eveng=((given_time>=16) and (given_time<20))
if morning:
    print("Good Morning")
elif afternoon:
    print("Good Afternoon")
elif eveng:
    print("Good Evening")
else:
    print("Good Night")
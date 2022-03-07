given_month=int(input())

winter_months=((given_month==11) or (given_month==12) or (given_month==1))
spring_months=((given_month==2) or (given_month==3))
summer_months=((given_month==4) or (given_month==5) or (given_month==6))
rainy_months=((given_month==7) or (given_month==8))

if winter_months:
    print("Winter")
elif spring_months:
    print("Spring")
elif summer_months:
    print("Summer")
elif rainy_months:
    print("Rainy")
else:
    print("Autumn")

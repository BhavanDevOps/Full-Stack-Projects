given_input=input()
given_second_input=input()

length=len(given_input)
given_input=given_input[ :(length-1)]
given_input=int(given_input)

if (given_input>=75):
    print("Allowed to write exam")
elif (given_input<75) and given_second_input=="Y":
    print("Allowed to write exam ")
else:
    print("Cannot write exam")
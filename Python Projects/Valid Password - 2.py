password=input()

is_all_lower=(password.lower()==password)
if is_all_lower:
    print("Invalid Password")
else:
    print("Valid Password")
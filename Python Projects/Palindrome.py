a=input()
a=a.lower()
reverse_a=""
for char in a:
    reverse_a=char+reverse_a
if a==reverse_a:
    print("Palindrome")
else:
    print("Not a Palindrome")
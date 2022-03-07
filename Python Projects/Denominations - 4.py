Denominations = (2000, 500, 200, 50, 20, 5, 2, 1)
amount = int(input())
output = {}
for n in Denominations:
	output[n] = amount  //n
	amount %= n
for k, v in output.items():
	print(k, v, sep=':', end=" ")
print()
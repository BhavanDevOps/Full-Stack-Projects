nominals = (1000, 500, 100, 500, 50, 10, 1)
amount = int(input())
output = {}
for n in nominals:
	output[n] = amount // n
	amount %= n
for k, v in output.items():
	print(k, v, sep=':')
print()	
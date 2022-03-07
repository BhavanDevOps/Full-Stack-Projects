A = int(input())
if A % 10 != 0:
    raise ValueError('The number must be divisible by 10 without a remainder')
print('100 Notes:', A//100)
A -= A//100 * 100
print('50 Notes:', A//50)
A -= A//50 * 50
print('20 Notes:', A//20)
A -= A//20 * 20
print('10 Notes:', A//10)
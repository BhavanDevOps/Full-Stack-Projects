N = int(input())
for i in range(N+1):
    print('_', end='')
print()
for i in range(N):
    print('|', end='')
    print(' ' * (N - i - 1), end='')
    print('/')
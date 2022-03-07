N = int(input())

pattern = []
for i in range(1, N + 1):
    pattern.append(' '.join(['*' for _ in range(i)]))
print('\n'.join(pattern))
print('\n'.join(pattern))
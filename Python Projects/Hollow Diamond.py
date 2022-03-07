N = int(input())

left = N-1
mid = -1
ch = 'A'
print(' '*left, ch, sep='')

for _ in range(N-1):
    left -= 1
    mid += 2
    ch = chr(ord(ch)+1)
    print(' '*left, ch, ' '*mid, ch, sep='')
    
for _ in range(N-2):
    left += 1
    mid -= 2
    ch = chr(ord(ch)-1)
    print(' '*left, ch, ' '*mid, ch, sep='')

left += 1
ch = 'A'
print(' '*left, ch, sep='')
full_string=input()
subsequence=input()
subseq_index=0
subseq_len=len(subsequence)
for char in full_string:
    if char==subsequence[subseq_index]:
        subseq_index+=1
    if subseq_index==subseq_len:
        break
if subseq_index==subseq_len:
    print("Yes")
else:
    print("No")

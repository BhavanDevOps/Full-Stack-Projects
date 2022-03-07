T = input()
S=T[-1]
T=T[0:len(T)-1]
T=float(T)

if S=='C':
	F=(9/5)*float(T) + 32
	print(str(T)+"C")
	print(str(F)+"F")
	k=((float(T)+273))
	k=float(k)
	print(str(k)+"K")
	
elif S=='F':
	C=(float(T)-32)*(5/9)
	K=C+273
	k=(round(K,2))
	c=(round(C,2))
	print(str(c)+"C")
	print(str(T)+"F")
	print(str(k)+"K")

elif S=='K':
	C=float(T)-273
	F=(9/5)*float(C) + 32
	
	c=(round(C,2))
	print(str(c)+"C")
	f=(round(F,2))
	print(str(f)+"F")
	print(str(T)+"K")
else: 
	print("None")
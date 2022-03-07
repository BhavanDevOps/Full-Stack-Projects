def getSum(x, membership):
   i = 1
   sumSeries = 0  
   for member in range(membership):
      if member % 2 > 0:
         sumSeries += -x**i
         i += 2
      else:
         sumSeries += x**i
         i += 2
   return sumSeries

x = int(input())
membership = int(input())
print(getSum(x, membership))
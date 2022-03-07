nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
n=int(input())

count_occurrences=nums_list.count(n)

for i in range(count_occurrences):
    nums_list.remove(n)
    
print(nums_list)
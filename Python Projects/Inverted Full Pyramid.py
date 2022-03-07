num_of_rows=int(input())
for i in range(num_of_rows):
    left_spaces=" "*i
    stars="* "*(num_of_rows-i)
    print(left_spaces+stars)
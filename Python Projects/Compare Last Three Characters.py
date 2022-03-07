first_string=input()
second_string=input()
#index_of_first_string=first_string[0:5]
#index_of_second_string=second_string[0:7]
#iscompare=index_of_second_string==index_of_second_string
#print(iscompare)
if first_string[len(first_string)-1]==second_string[len(second_string)-1]and first_string[len(first_string)-2]==second_string[len(second_string)-2]and first_string[len(first_string)-3]==second_string[len(second_string)-3]:
    print("True")
else:
    print("False")
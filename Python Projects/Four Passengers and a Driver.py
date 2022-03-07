def number_of_cars_needed(no_of_people):
    # Complete this function
    number_of_cars=no_of_people//5
    remaining_people=no_of_people%5
    if remaining_people>0:
        number_of_cars+=1
    return number_of_cars
    
no_of_people = int(input())
# Call the number_of_cars_needed function
result=number_of_cars_needed(no_of_people)
print(result)
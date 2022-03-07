given_number_of_days=int(input())

years=given_number_of_days/365
years=int(years)
weeks=(given_number_of_days%365)/7
weeks=int(weeks)
days=(given_number_of_days%365)%7
days=int(days)

print(data)
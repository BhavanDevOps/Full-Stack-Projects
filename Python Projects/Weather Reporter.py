def get_weather_report(temp):
    # Complete this function
    if temp<22:
        weather="Cold"
    elif (temp>=22) and (temp<35):
        weather="Warm"
    else:
        weather="Hot"
    return weather
temp = int(input())
# Call the get_weather_report function

result=get_weather_report(temp)
print(result)

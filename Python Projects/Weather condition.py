def get_weather_report (T):
    if T<0:
        return "Freezing weather"
    if T>=0 and T<10:
        return "Very Cold weather"
    if T>=10 and T<20:
        return "Cold weather"
    if T>=20 and T<30:
        return "Normal"
    if T>=30 and T<40:
        return "Hot"
    if T>=40:
        return "Very Hot"


T= float(input())
print(get_weather_report(T))
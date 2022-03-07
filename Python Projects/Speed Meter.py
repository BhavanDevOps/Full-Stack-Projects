def get_speed_status(speed):
    # Complete this function
    if speed<60:
        msg="Normal"
    elif (speed>=60)and (speed<80):
        msg="Warning"
    else:
        msg="Over Speed"
    return msg

speed = int(input())
# Call the get_speed_status function
result=get_speed_status(speed)
print(result)
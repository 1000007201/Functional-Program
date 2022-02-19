
def wind(t,v):
    '''
    It takes value of temperature and wind speed as parameter and returns wind chill speed.
    :param t: temperature
    :param v: Wind Speed
    :return: Wind Chill Speed
    '''
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*(v**0.16)
    return w


temp = float(input("Enter value of Temperature less than 50:"))
wind_speed = float(input("Enter value of Wind Speed between 3 and 120:"))

if(temp < 50 and 3 < wind_speed < 120):
    wind_chill_speed = wind(temp,wind_speed)
    print(f"Speed of Wind Chill: {wind_chill_speed}")
else:
    print("Enter Correct Value.")
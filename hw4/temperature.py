def convert_cel_to_far(cel: float) -> float: 
    fah = cel * 9 / 5 + 32
    return fah
def convert_far_to_cel(fah: float) -> float:
    cel = (fah - 32) * 5 / 9
    return cel
t2 = float(input('Enter a temperature in degrees F: '))
print(t2, ' degress in Fahrenheit = ', round(convert_far_to_cel(t2), 2), ' degrees in Celsius')
t1 = float(input('Enter a temperature in degrees C: '))
print(t1, ' degress in Celcius = ', round(convert_cel_to_far(t1), 2), ' degrees in Fahrenheit')
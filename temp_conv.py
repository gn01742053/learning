temp = input('Please input temperature: ')
unit = input('Please input original unit(F or C): ')
temp = float(temp)

if unit == 'F':
    temp = (temp - 32) * 5 / 9
    unit = 'C'
elif unit == 'C':
    temp = temp * 9 / 5 + 32
    unit = 'F'
print(temp, unit)

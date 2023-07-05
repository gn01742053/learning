height = input('Please input height: ')
weight = input('Pleser input weight: ')
height = float(height)
height = height / 100
weight = float(weight)
bmi = weight / (height * height)
if bmi < 18.5:
    print('過輕')
elif bmi >= 18.5 and bmi < 24:
    print('正常')
elif bmi >= 24 and bmi < 27:
    print('過重')
else:
    print('肥胖')
print(bmi)

print('calculator')

def add(x, y):
    return(x+y)

def add2(x,y):
    return(x-y)

num1 = int(input('1-sonni kiriting:'))
num2 = int(input('2-sonni kiriting:'))

num3 = add(num1, num2)
num4 = add2(num1, num2)

print("Sonlar yig'indisi:" + str(num3))
print("Sonlar ayirmasi:" + str(num4))

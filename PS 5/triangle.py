#
# triangle.py
#
# A program to compute information about right triangles.

import math

a = int(input('Enter the first leg to the nearest inch: '))
b = int(input('Enter the second leg to the nearest inch: '))
print()

if a <= 0 or b <= 0:
    print('The lengths must be positive.')
else:
    hypotenuse = round(math.sqrt(a ** 2 + b ** 2), 2)
    area = round(a * b / 2, 1)
    print('The hypotenuse is:', hypotenuse, 'inches')
    print('The area is:', area, 'sq in')
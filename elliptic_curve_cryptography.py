from finite_field import FieldElement
from elliptic_curve import Point

'''
CH3, Exercise 1:

  Evaluate whether the points (192,105), (17,56), (200,119), (1,193), and (42,99) are on the curve y**2 = x**3 + 7 over F_223:

def CH3_Exercise_1():

  for point in [(192,105), (17,56), (200,119), (1,193), (42,99)]:
    print(FieldElement(point[1],223)**2 == FieldElement(point[0],223)**3 + FieldElement(7,223))

CH3_Exercise_1()

>>> True
>>> True
>>> False
>>> True
>>> False
'''

'''
CH3, Example 1:

a = FieldElement(num=0, prime=223)
b = FieldElement(num=7, prime=223)
x = FieldElement(num=192, prime=223)
y = FieldElement(num=105, prime=223)
p1 = Point(x, y, a, b)
print(p1)

>>> Point(192,105)_0_7 FieldElement(223)
'''

'''
CH3, Example 3:

prime = 223
a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)
x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)
x2 = FieldElement(num=17, prime=prime)
y2 = FieldElement(num=56, prime=prime)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print(p1+p2)

>>> Point(170,142)_0_7 FieldElement(223)
'''

'''
CH3, Exercise 2:

  For the curve y**2 = x**3 + 7 over F_223, find:

    a)   (170,142) + (60,139)
    b)   (47,71) + (17,56)
    c)   (143,98) + (76,66)

def CH3_Exercise_2():
  prime = 223
  a = FieldElement(0, prime)
  b = FieldElement(7, prime)

  for points in [[(170,142), (60,139)], [(47,71), (17,56)], [(143,98), (76,66)]]:
    p1 = Point(FieldElement(points[0][0], prime), FieldElement(points[0][1], prime), a, b)
    p2 = Point(FieldElement(points[1][0], prime), FieldElement(points[1][1], prime), a, b)
    print(p1+p2)

CH3_Exercise_2()

>>> Point(220,181)_0_7 FieldElement(223)
>>> Point(215,68)_0_7 FieldElement(223)
>>> Point(47,71)_0_7 FieldElement(223)
'''

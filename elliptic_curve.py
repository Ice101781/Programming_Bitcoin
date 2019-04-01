'''
Elliptic curves have the following form:

  y**2 = x**3 + a*x + b

Specifically, the elliptic curve used in Bitcoin is called 'secp256k1' and it uses this particular equation:

  y**2 = x**3 + 7,

so the curve is defined by the constants a=0, b=7.


Point Addition:

  It turns out that for every elliptic curve, a line will intersect it at either one point or three points,
  except in a couple of special cases. These two cases are when a line is exactly vertical and when a line
  is tangent to the curve.

  We can define point addition using the fact that lines intersect one or three times with the elliptic
  curve. Two points define a line, so since that line must intersect the curve one more time, that third
  point reflected over the x-axis is the result of the point addition.

  So, for any two points P1 = (x1, y1) and P2 = (x2, y2), we get P1 + P2 as follows:

    - Find the point intersecting the elliptic curve a third time by drawing a line through P1 and P2.
    - Reflect the resulting point over the x-axis.

  In mathematics parlance, point addition is non-linear.

  Point addition satisfies certain properties that we associate with addition, such as:

    1) Identity:

        There's a 'zero'. That is, there exists some point I that, when added to a point A, results in A so that:

          I + A = A.

        We'll call this point the 'point at infinity'. (This is related to Invertibility.)


    2) Commutativity:

        This is obvious since the line going through A and B will intersect the curve a third time in the same
        place, no matter the order.

          A + B = B + A.


    3) Associativity:

        This isn't obvious and is the reason for flipping over the x-axis.

          (A + B) + C = A + (B + C).


    4) Invertibility:

        For some point A, there's some other point -A that results in the identity point, I. That is:

          A + (-A) = I.

        Visually, these points are opposite one another over the x-axis on the curve so that a vertical line passes
        through them.


  To code point addition, we're going to split it up into three steps:

    a) Where the points are in a vertical line, or using the identity point

    b) Where the point are not in a vertical line, but are different

    c) Where the two points are the same
'''

class Point:

  def __init__(self, x, y, a, b):
    self.a = a
    self.b = b
    self.x = x
    self.y = y
    if self.x is None and self.y is None:
      return
    # We check here that the point is actually on the curve
    if self.y**2 != self.x**3 + self.a*self.x + self.b:
      raise ValueError('({}, {}) is not on the curve'.format(self.x, self.y))

  # '==' operator; Points are equal if and only if they are on the same curve and have the same coordinates
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y \
      and self.a == other.a and self.b == other.b

  # CH 2, Exercise 2 - '=/=' operator
  def __ne__(self, other):
    # this should be the inverse of the '==' operator
    return not (self == other)


# CH 2, Example 1:
p1 = Point(-1, -1, 5, 7)
# No error, point is on the curve
## p2 = Point(-1, -2, 5, 7)  <-- SUPPRESSED SINCE IT RAISES AN ERROR
# ValueError: (-1, -2) is not on the curve


'''
CH 2, Exercise 1:

  Determine which of these points are on the curve y**2 = x**3 + 5x + 7:

    1) (2, 4)

    2) (-1, -1)

    3) (18, 77)

    4) (5, 7)
'''
def CH2_Exercise_1(x, y):

  print(y**2 == x**3 + 5*x + 7)

CH2_Exercise_1(2, 4)
# False
CH2_Exercise_1(-1, -1)
# True
CH2_Exercise_1(18, 77)
# True
CH2_Exercise_1(5, 7)
# False
'''

'''

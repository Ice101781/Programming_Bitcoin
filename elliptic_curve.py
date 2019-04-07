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


  To code point addition, P1 + P2 = P3 ==> (x1, y1) + (x2, y2) = (x3, y3), we're going to split it up into three steps:

    A) Where the points are in a vertical line, or using the identity point


    B) Where the points are not in a vertical line, but are different:

        Let's start with the fact that the line goes through P1 = (x1, y1) and P2 = (x2, y2), and has this formula:

            s = (y2 - y1) / (x2 - x1), so

            y = s*(x - x1) + y1.

        The second formula is the equation of the line that intersects at both P1 and P2. Using this formula and plugging
        it into the elliptic curve equation, we get:

            y**2 == (s*(x - x1) + y1)**2 = x**3 + a*x + b.

        Gathering all the terms, we have this polynomial equation:

            x**3 - s**2*x**2 + (a + 2*s**2*x1 - 2*s*y1)*x + b - s**2*x1**2 + 2*s*x1*y1 - y1**2 = 0.

        Since the elliptic curve is intersected by our line, x1, x2, and x3 must be roots of this equation, thus:

            (x - x1)*(x - x2)*(x - x3) = 0, so

            x**3 - (x1 + x2 + x3)*x**2 + (x1*x2 + x1*x3 + x2*x3)*x - x1*x2*x3 = 0.

        There's a result from what's called 'Vieta's formula', which states that the coefficients have to equal each other
        if the roots are the same. The first coefficient that's interesting is the coefficient in front of x**2:

            -s**2 = -(x1 + x2 + x3), so

            x3 = s**2 - x1 - x2.

        We can plug this expression into the formula for the line above, but remember, we have to reflect over the x-axis,
        so the right side has to be negated:

            y3 = -(s*(x3 - x1) + y1) == s*(x1 - x3) - y1.

        QED.


    C) Where the two points are the same, such that P1 + P1 == P3:

        Visually, we have to calculate the line that's tangent to the curve at P1 and find the point at which the line
        intersects the curve. Once again we'll need to find the slope, though this time, for the tangent point. This will
        require some calculus. We take the derivative of both sides of the elliptic curve equation with respect to x:

            d( y**2 ) / dx == d( x**3 + a*x + b ) / dx

            2*y * dy/dx == 3*x**2 + a

            dy/dx == (3*x**2 + a) / (2*y).

        The rest of the formula goes through as before, except x1 = x2, so we can combine them:

            x3 = s**2 - 2*x1, and

            y3 = s*(x1 - x3) - y1.
'''

class Point:

  def __init__(self, x, y, a, b):
    self.a = a
    self.b = b
    self.x = x
    self.y = y
    # handling for the point at infinity
    if self.x is None and self.y is None:
      return
    # only check to see if the point is on the curve if we have values for x and y
    if self.y**2 != self.x**3 + self.a*self.x + self.b:
      raise ValueError('({}, {}) is not on the curve'.format(self.x, self.y))

  # '==' operator; Points are equal if and only if they are on the same curve and have the same coordinates
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y \
      and self.a == other.a and self.b == other.b

  # CH 2, Exercise 2: '=/=' operator
  def __ne__(self, other):
    # this should be the inverse of the '==' operator
    return not (self == other)

  # string representation of Point object
  def __repr__(self):
    if self.x is None:
      return 'Point(infinity)'
    else:
      return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

  # '+' operator
  def __add__(self, other):
    # two points must lie on the same curve in order to add them together
    if self.a != other.a or self.b != other.b:
      raise TypeError('Points {}, {} are not on the same curve'.format(self, other))
    '''
    CASE WHEN x1 == x2 (vertical line, infinite slope)
    '''
    # handle identity point (additive identity)
    if self.x is None:
      return other
    if other.x is None:
      return self
    '''
    CH2, Exercise 3: Handle the case where the two points are additive inverses. That is, they have the same x,
    but a different y, causing a vertical line. This should return the point at infinity.
    '''
    if self.x == other.x and self.y != other.y:
      return self.__class__(None, None, self.a, self.b)
    '''
    CASE WHEN x1 =/= x2 (sloping line)

    CH2, Exercise 5:
    '''
    if self.x != other.x:
      # slope of the line formed by self and other
      s = (other.y - self.y) / (other.x - self.x)
      # x coordinate of the new point
      x = s**2 - self.x - other.x
      # y coordinate of the new point
      y = s*(self.x - x) - self.y
      # return an instance of the class to make subclassing easier
      return self.__class__(x, y, self.a, self.b)
    '''
    CASE WHEN P1 == P2 (tangent line)

    CH2, Exercise 7:
    '''
    if self == other:
      s = (3*self.x**2 + self.a) / (2*self.y)
      x = s**2 - 2*self.x
      y = s*(self.x - x) - self.y
      return self.__class__(x, y, self.a, self.b)
    '''
    One more exception...

    CASE WHEN P1 == P2 && P1[1] = 0 (tangent and vertical line)
    '''
    if self == other and self.y == 0:
      # return the point at infinity
      return self.__class__(None, None, self.a, self.b)


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
CH2, Example 2:

  When coding point addition, we first handle the identity point, or point at infinity. Since we can't easily
  use infinity in Python, we'll use the 'None' value instead. What we want is this to work:

    p1 = Point(-1, -1, 5, 7)
    p2 = Point(-1, 1, 5, 7)
    inf = Point(None, None, 5, 7)

    >>> print(p1 + inf)
    Point(-1,-1)_5_7

    >>> print(inf + p2)
    Point(-1,1)_5_7

    >>> print(p1 + p2)
    Point(infinity)


CH2, Exercise 4:

  For the curve y**2 = x**3 + 5*x + 7, what is (2,5) + (-1,-1)?
'''
def CH2_Exercise_4(P1, P2):

  '''
  P1 + P2 = P3 == (x3, y3)
  x3 = s**2 - x1 - x2
  y3 = s*(x1 - x3) - y1
  '''
  s = (P2[1] - P1[1]) / (P2[0] - P1[0])
  x3 = s**2 - P1[0] - P2[0]
  y3 = s*(P1[0] - x3) - P1[1]
  print(x3, y3)

CH2_Exercise_4((2,5), (-1,-1))
# (3, -7)
'''
CH2, Exercise 6:

  For the curve y**2 = x**3 + 5*x + 7, what is (-1,-1) + (-1,-1)?
'''
def CH2_Exercise_6(P1):

  '''
  P1 + P1 = P3 == (x3, y3)
  x3 = s**2 - 2*x1
  y3 = s*(x1 - x3) - y1
  '''
  s = (3*P1[0]**2 + 5) / (2*P1[1])
  x3 = s**2 - 2*P1[0]
  y3 = s*(P1[0] - x3) - P1[1]
  print(x3, y3)

CH2_Exercise_6((-1,-1))
# (18, 77)

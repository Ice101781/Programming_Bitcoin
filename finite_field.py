'''
A finite field is defined as a bounded set of numbers and
two operations, '+' (addition) and '*' (multiplication),
that satisfy the following:

1.) If a and b are in the set, a + b and a * b are in the
set. That is, the set is closed under addition and
multiplication.

2.) 0 exists and has the property a + 0 = a. This is called
the additive identity.

3.) 1 exists and has the property a * 1 = a. This is called
the multiplicative identity.

4.) If a is in the set, -a is in the set, which is defined
as the value that a + (-a) = 0. This is called the
additive inverse.

5.) If a is in the set and is not 0, a^(-1) is in the set,
which is defined as the value that makes a * a^(-1) = 1.
This is called the multiplicative inverse.
'''

class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    # Exercise 1
    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)

# test
a = FieldElement(7, 13)
b = FieldElement(6, 13)

print(a == b)
# False
print(a == a)
# True

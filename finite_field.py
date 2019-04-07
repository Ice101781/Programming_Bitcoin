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

    # string representation
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    # '==' operator
    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    # CH1, Exercise 1: '=/=' operator
    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)

    # '+' operator
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    # CH1, Exercise 3: '-' operator
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        # return an element of the same class
        return self.__class__(num, self.prime)

    # CH1, Exercise 6: '*' operator <-- NEED TO VERIFY THIS ANSWER
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        '''
        '(self.num ** exponent) % self.prime' is less efficient than the expression below, because with
        'pow(self.num, exponent, self.prime)', the modulo function is done after each round of multiplication.

        Naive implementation of negative exponents:
        n = exponent
        while n < 0:
            n += self.prime - 1

        Better implementation of negative exponents:
        '''
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    # CH1, Exercise 9: '/' operator <-- NEED TO VERIFY THIS ANSWER
    # why doesn't '__truediv__' work here?
    def __div__(self, other):
        '''
        Here we make use of 'Fermat's Little Theorem':

            n**(p-1) % p == 1.

        Under finite field exponentiation, we have:

            n**(p-1) == 1.

        So,

            a/n == a * n**(-1) == a * (n**(-1) * 1) == a * (n**(-1) * n**(p-1)) == a * n**(p-2).
        '''
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        # Jimmy's implementation of this is a little different
        num = (self.num * other.num**(self.prime-2)) % self.prime
        return self.__class__(num, self.prime)


# test
a = FieldElement(7, 13)
b = FieldElement(6, 13)

print(a == b)
# False
print(a == a)
# True

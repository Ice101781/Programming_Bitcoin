from finite_field import FieldElement

'''
"In abstract algebra, a congruence relation (or simply congruence) is an equivalence relation on an algebraic structure
(such as a group, ring or vector space) that is compatible with the structure in the sense that algebraic operations
done with equivalent elements will yield equivalent elements. Every congruence relation has a corresponding quotient
structure, whose elements are the equivalence classes (or congruence classes) for the relation."

   --- Wikipedia (Congruence relation)

"Modular arithmetic can be handled mathematically by introducing a congruence relation on the integers that is compatible
with the operations on the integers: addition, subtraction, and multiplication. For a positive integer n, two numbers
a and b are said to be congruent modulo n, if their difference a - b is an integer multiple of n (that is, if there is an
integer k such that a - b = k * n). This congruence relation is typically considered when a and b are integers, and is
denoted a = b mod n. ...this generally means that mod denotes the modulo operation, that is 0 <= a < n. The number n is
called the modulus of congruence. The congruence relation may be rewritten as a = (k * n) + b, explicitly showing its
relationship with Euclidean division."

   --- Wikipedia (Modular arithmetic)

Example 1:

   If 1 = 7 mod 3,

      1 - 7 = k * 3, then k = -2.

   Note that (1 = 7 mod 3) == (7 % 3 = 1).


Example:

   It is currently 3 o'clock. What hour was it 16 hours ago?

   (3 - 16) % 12 = x  ==  x = (3 - 16) mod 12

                          x - (3 - 16) = k * 12

                          x + 13 = k * 12

   How can we solve this one equation that contains two unknowns? We have a restraint on the value of x: 0 <= x < 12. So,
   if we choose k = 2, we have:

                          x + 13 = (2) * 12

                          x = 11.

   Suppose instead that we wanted to know what hour it will be 16 hours after 3 o'clock. We have:

   (3 + 16) % 12 = x  ==  x = (3 + 16) mod 12

                          x - (3 + 16) = k * 12

                          x - 19 = k * 12

   If we choose k = 2 then x = 43, but recall that 0 <= x < 12. So choose k = -1:

                          x - 19 = (-1) * 12

                          x = 7.
'''

print(7 % 3)
# 1
print(-27 % 13)
# 12


'''
Finite Field Addition / Subtraction

  for a,b in F_p, we have:

      a + f_b = (a + b) % p

      a - f_b = (a - b) % p


  CH1, Exercise 2:

    Solve the following problems in F_57:

      1)  44 + f_33 = (44 + 33) % 57

                    = 77 % 57

                    => x = 77 mod 57

                       x - 77 = k * 57  (choose k = -1)

                       x = 77 + (-1) * 57

                       x = 20.


      2)  9 - f_29 = (9 - 29) % 57

                   = -20 % 57

                   => x = -20 mod 57

                      x - (-20) = k * 57  (choose k = 1)

                      x = -20 + (1) * 57

                      x = 37.


      3)  17 + f_42 + f_49 = (17 + 42 + 49) % 57

                           = 108 % 57

                           => x = 108 mod 57

                              x - 108 = k * 57  (choose k = -1)

                              x = 108 + (-1) * 57

                              x = 51.


      4)  52 - f_30 - f_38 = (52 - 30 - 38) % 57

                           = -16 % 57

                           => x = -16 mod 57

                              x - (-16) = k * 57  (choose k = 1)

                              x = -16 + (1) * 57

                              x = 41.


  CH1, Exercise 4:

    Solve the following equations in F_97:

      1)  95 * f_45 * f_31 = (95 * 45 * 31) % 97

                           = 132,525 % 97

                           = 23.


      2)  17 * f_13 * f_19 * f_44 = (17 * 13 * 19 * 44) % 97

                                  = 184,756 % 97

                                  = 68.


      3)  12^7 * f_77^49 = (12^7 * 77^49) % 97

                         =>
'''
print((12**7 * 77**49) % 97)
'''
                         = 63.


  CH1, Exercise 5:

    For k = 1,3,7,13,18, what is the set {k*0, k*1, k*3, ..., k*18} in F_19?
'''
def CH1_Exercise_5(order, k_list):

  for k in k_list:
    set = []
    for n in range(order):
      set.append(k * n % order)
    print(set)

CH1_Exercise_5(6, [1,3,7,13,18])
CH1_Exercise_5(19, [1,3,7,13,18])
'''
  A: "  The answer to Exercise 5 is why fields have to have a prime power number of elements. No matter what k you choose,
     as long as it's greater than 0, multiplying the entire set by k will result in the same set as you started with.

     Intuitively, the fact that we have a prime order results in every element of a finite field being equivalent. If
     the order of the set was a composite number, multiplying the set by one of the divisors would result in a smaller set."

    For order = 6:

      [0, 1, 2, 3, 4, 5]
      [0, 3, 0, 3, 0, 3]  <-- smaller set because (k = 3) divides (order = 6) evenly
      [0, 1, 2, 3, 4, 5]
      [0, 1, 2, 3, 4, 5]
      [0, 0, 0, 0, 0, 0]  <-- smaller set because (k = 18) is an integer multiple of (order = 6)

    For order = 19:

      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
      [0, 3, 6, 9, 12, 15, 18, 2, 5, 8, 11, 14, 17, 1, 4, 7, 10, 13, 16]
      [0, 7, 14, 2, 9, 16, 4, 11, 18, 6, 13, 1, 8, 15, 3, 10, 17, 5, 12]
      [0, 13, 7, 1, 14, 8, 2, 15, 9, 3, 16, 10, 4, 17, 11, 5, 18, 12, 6]
      [0, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


  CH1, Exercise 7:

    For p = 7,11,17,31, what is the set {1^(p-1), 2^(p-1), 3^(p-1), 4^(p-1), ..., p-1^(p-1)} in F_p?
'''
def CH1_Exercise_7(prime_list):

  for p in prime_list:
    set = []
    for n in range(1,p):
      set.append(FieldElement(n,p) ** (p-1))
    print(set)

CH1_Exercise_7([7,11,17,31])
'''
  A: The set is always {FieldElement_p(1)}, or a list containing p-1 FieldElement_p(1)'s.

     "In case you didn't get it, the answer is that n^(p-1) is always 1 for every p that is prime and every n > 0.
     This is a beautiful result from number theory called Fermat's Little Theorem. Essentially, the theorem says:
     n^(p-1) % p = 1, where p is prime."

    [FieldElement_7(1), FieldElement_7(1), FieldElement_7(1), FieldElement_7(1), FieldElement_7(1), FieldElement_7(1)]

    [FieldElement_11(1), FieldElement_11(1), FieldElement_11(1), FieldElement_11(1), FieldElement_11(1), FieldElement_11(1),
     FieldElement_11(1), FieldElement_11(1), FieldElement_11(1), FieldElement_11(1)]

    [FieldElement_17(1), FieldElement_17(1), FieldElement_17(1), FieldElement_17(1), FieldElement_17(1), FieldElement_17(1),
     FieldElement_17(1), FieldElement_17(1), FieldElement_17(1), FieldElement_17(1), FieldElement_17(1), FieldElement_17(1),
     FieldElement_17(1), FieldElement_17(1), FieldElement_17(1), FieldElement_17(1)]

    [FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1),
     FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1),
     FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1),
     FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1),
     FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1), FieldElement_31(1)]


  CH1, Exercise 8:

    Solve the following equations in F_31:  <-- NEED TO VERIFY THESE ANSWERS

      1)  3 / f_24 = 3 * f_24**(-1)

                   = 3 * f_24**(31-2)

                   =>
'''
print((3 * 24**29) % 31)
print(FieldElement(3,31) * FieldElement(24,31)**29)
print('The following is a test of the solution to CH1, Exercise 9:')
print(FieldElement(3,31) / FieldElement(24,31))
'''
                   = 4.


      2)  f_17^(-3) = 17**(-1) * f_17**(-1) * f_17**(-1)

                    = 17**(31-2) * f_17**(31-2) * f_17**(31-2)

                    = f_17**(29*3)

                    =>
'''
print((17**87) % 31)
print(FieldElement(17,31)**87)
'''
                    = 29.


      3)  4^(-4) * f_11 = (4**(-1) * f_4**(-1) * f_4**(-1) * f_4**(-1)) * f_11

                        = 4**((31-2)*4) * f_11

                        =>
'''
print((4**116 * 11) % 31)
print(FieldElement(4,31)**116 * FieldElement(11,31))
'''
                        = 13.
'''

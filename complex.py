"""
Write a program to perform the following operations on complex numbers
using class, object and constructor.
(a) Addition
(b) Subtraction
(c) Multiplication
(d) Check if two complex numbers are equal or not
(e) Check if C1 >= C2
(f) Check if C1 <= C2
"""

class Complex:
    def _init_(self,r,i):
        self.r=r;
        self.i=i;
    def add(self,c1,c2):
        temp=Complex(0,0)
        temp.r=c1.r+c2.r
        temp.i=c1.i+c2.i
        print("Sum of two Complex numbers : ",temp.r,"+i",temp.i)
    def sub(self,c1,c2):
        temp = Complex(0, 0)
        temp.r = c1.r - c2.r
        temp.i = c1.i - c2.i
        print("Difference of two number : ",temp.r, "+i", temp.i)
    def multi(self,c1,c2):
        C1=complex(c1.r,c1.i)
        C2=complex(c2.r,c2.i)
        c3=C1*C2
        print("Multiplication of two number : ",c3.real,"+i",c3.imag)
    def is_equal(self, c1, c2):
        C1=complex(c1.r,c1.i)
        C2=complex(c2.r,c2.i)
        if C1 == C2:
          print("Two complex numbers are equal.")
        else:
          print("Two complex numbers are not equal.")
    def is_c1greaterC2(self, c1, c2):
       modC1 = abs(complex(c1.r,c1.i))
       modC2 = abs(complex(c2.r,c2.i))
       print("C1 >= C2 : ", end = " ")
       if modC1 >= modC2:
         print(True)
       else:
         print(False)
    def is_C1lesserC2(self, c1, c2):
       modC1 = abs(complex(c1.r,c1.i))
       modC2 = abs(complex(c2.r,c2.i))
       print("C1 <= C2 : ", end = " ")
       if modC1 <= modC2:
         print(True)
       else:
         print(False)
print("Enter the real and imaginary part of complex number 1 : ")
r=int(input())
i=int(input())
c1=Complex(r,i)
print("Enter the real and imaginary part of complex number 2 : ")
r=int(input())
i=int(input())
c2=Complex(r,i)
c=Complex(0,0)
c.add(c1,c2)
c.sub(c1,c2)
c.multi(c1,c2)
c.is_equal(c1,c2)
c.is_c1greaterC2(c1, c2)
c.is_C1lesserC2(c1, c2)

"""
Enter the real and imaginary part of complex number 1 : 
-6
5
Enter the real and imaginary part of complex number 2 : 
9
-4
Sum of two Complex numbers :  3 +i 1
Difference of two number :  -15 +i 9
Multiplication of two number :  -34.0 +i 69.0
Two complex numbers are not equal.
C1 >= C2 :  False
C1 <= C2 :  True
"""
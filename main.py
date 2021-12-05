from sympy import *

x = symbols('x')

a = Integral(cos(x)*exp(x), x)



print ("x=",x)

print ("a=",a)

print (Eq(a, a.doit()))



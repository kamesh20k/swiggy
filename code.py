# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 2
b = 6
c = 9
d = 7
# calculate the discriminant
e = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(e))/(4*a)
sol2 = (-b+cmath.sqrt(e))/(4*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


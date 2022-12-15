
# Quadratic equation

import cmath

a = 1
b = 5
c = 6

# Formula
#(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# calculate the discriminant
d = (b**2) - (4*a*c)
# find solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution is {0} and {1}'.format(sol1,sol2))

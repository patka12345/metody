from cs50 import get_int
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# TASKS (8p)- calculate & print:
print('#0 Use alternative way of reading inputs - using library (0.5p)\n')

x = get_int("radius of first circle (X): ")                 #function allows a user to enter only integer
y = get_int("radius of second circle (Y): ")

print('\n#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)')
# values are taken from task #0, where domain is narrowed to integers
# As radius can be also positive float number, it's possible to use input() function, which return string, which has to be changed to float by float() function.

if x > 0 and y > 0:
    print('for radius X =', x, 'and radius Y =', y)
    print('perimeter of first circle: ', 2*np.pi*x)
    print('perimeter of second circle: ', 2*np.pi*y)
    print('field of first circle: ', np.pi*x**2)
    print('field of second circle: ', np.pi*y**2)
else:
    print('X or Y are not positive number')

print('\n#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)\n')

x = 1
while not x%2 == 0:
    x = np.random.randint(100)

y = 1
while not(y%2==0 and x%y==0):
    y += 1

print('X =',x)
print('Y =',y)

print("""\n#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.\n""")

x = np.random.randint(100)
y = np.random.randint(100)
print('X =', x, 'Y =', y)
print('X is divisible by Y' if x % y == 0 else 'X is not divisible by Y')

print('\n#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)')
print('In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)\n')

# program takes values from task #3. Works for any other pair of floats.

div1 = Decimal(x/y)
div1 = round(div1,2)
print(div1)

print("""\n#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
it's totally up to your imagination how do you want to amend the figure according to the input number (1p)\n""")

# 1 - extension of range of a domain of a function
# 2 - R is calculated by different formula
# 3 - opposite function

choice = get_int('choose 1,2 or 3:')
choice = int(choice)
a = 1
b = 1

while True:
    if choice == 1:
        a = 2
        x_knots = np.linspace(a * (-3 * np.pi), a * (3 * np.pi), 201)
        y_knots = np.linspace(a * (-3 * np.pi), a * (3 * np.pi), 201)
        X, Y = np.meshgrid(x_knots, y_knots)
        R = np.sqrt(X ** 2 + Y ** 2)
    elif choice == 2:
        x_knots = np.linspace(a * (-3 * np.pi), a * (3 * np.pi), 201)
        y_knots = np.linspace(a * (-3 * np.pi), a * (3 * np.pi), 201)
        X, Y = np.meshgrid(x_knots, y_knots)
        R = (X**2+Y**2)/2
    elif choice == 3:
        x_knots = np.linspace(a * (-3 * np.pi), a * (3 * np.pi), 201)
        y_knots = np.linspace(a * (-3 * np.pi), a * (3 * np.pi), 201)
        X, Y = np.meshgrid(x_knots, y_knots)
        R = np.sqrt(X ** 2 + Y ** 2)
        b = -1
    else:
        print('wrong value!')
        break

    Z = np.cos(R)**2*np.exp(-0.1*R)*b
    ax = Axes3D(plt.figure(figsize=(8,5)))
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
    plt.show()
    break

print('\n#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?')


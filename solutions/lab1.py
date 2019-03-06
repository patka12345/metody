from decimal import *
import math
import numpy as np
import matplotlib.pyplot as plt
#TASKS (4p)

#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

print('zbiór liczb:')
x = [i for i in range(56,101)]
print(x)
print('wartości funkcji:')
y = [2*i**2 + 2*i + 2 for i in x]
print(y,'\n')

#2 ask the user for a number and print its factorial (1p)

a = input('podaj liczbę naturalną: ')
print(a.isdigit())
if a.isdigit():
    a = int(a)
    fact = math.factorial(a)
    print(fact)
else:
    print('podana wartość jest nieprawidłowa')

# 3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

lista = np.array([[2,3,4,5,1], [2,1,4,5,6], [1,3,4,5,1]])
def min_arr(lista):
    in_min = lista.min()
    element = np.argwhere(lista == in_min)
    print('najmniejsza wartość to:', in_min)
    print('indeks(y) tej wartości to:\n', element)
    return(element, in_min)
min_arr(lista)

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)

a = input('wpisz licbę punktów (liczba naturlna bez 0): ')
a = int(a)
x = np.random.rand(a)*100
x = np.sort(x)
y = [a**3 for a in x]
plt.plot(x,y)
plt.show()

#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.

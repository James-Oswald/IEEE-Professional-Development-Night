#https://www.codewars.com/kata/58ce8725c835848ad6000007

#THIS IS THE WRONG SOLUTION, ask robin for the real one

from math import floor 

def potatoes(p0, w0, p1):
    return floor(w0 - ((p0 - p1)/100)*w0)

print(potatoes(99, 100, 98))
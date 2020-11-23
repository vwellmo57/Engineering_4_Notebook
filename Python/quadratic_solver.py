#Quadratic Solver
#Written by Vann W.
import array
import math
num = [1,1,1] #defining the arrays
roots = [1,2]
def solve(num): #defining the function
    discriminant = num[1] ** 2    #finding the discriminant
    discriminant = (discriminant)-(4*(num[0])*(num[2]))
    if (discriminant < 0):   #if the discriminant is <0 it returns no roots
      return("There are no real roots")
    else:   #if there are real roots
        roots[0] = math.sqrt(discriminant)    #solving the quadratic formula
        roots[0] = (-1*num[1]) - roots[0]     #first root 
        roots[0] = roots[0] / (2*num[0])  
        roots[0] = round(roots[0],2)
        roots[1] = math.sqrt(discriminant)  #second root
        roots[1] = (-1*num[1]) + roots[1]
        roots[1] = roots[1] / (2*num[0])  
        roots[1] = round(roots[1],2)
        return(roots)       #returns the roots as an array
print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")
num[0] = float(input("Enter A: ")) #gets user input
num[1] = float(input("Enter B: "))
num[2] = float(input("Enter C: "))
print("Roots:", solve(num))     #calling the function with an argument

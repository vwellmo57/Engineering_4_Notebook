def doMath(a,b,c): #defining the function and it's arguments
    if c==1:       #c tells the function what operation to do
        return(int(a) + int(b))   #where the math happens
    elif c==2:
        return (int(a) - int(b))  #have to make all answers int
    elif c==3:
        return (int(a) * int(b))
    elif c==4:
        d=float(a) / float(b)    #divide a by b, float is for decimals
        d=round(d,2)             #rounding the answer to 2 places
        return (d)
    elif c==5:
        return (int(a) % int(b))
    

a = input("Enter the first number: ")     #input for a and b
b = input("Enter the second number: ") 


print("Sum:\t\t" , doMath(a,b,1))        #calling the functions
print("Difference:\t" , doMath(a,b,2))   #I used a comma because 
print("Product:\t" , doMath(a,b,3))      #errors happen if I don't
print("Quotient:\t" , doMath(a,b,4))
print("Modulo:\t\t" , doMath(a,b,5))


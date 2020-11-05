# Engineering_4_Notebook
## Vann's Engineering 4 Stuff! :)
## Getting the Pi Online
I had to use a hotspot, set yours to 2.5 GHz under AP Band if, on android, this took me a while to figure out the hard way.
## Dice Roller
This assignment was a basic one I got the logic to work. I used a simple random function and an if statement to kill the program. I would recommend using an online compiler to write the code as it takes lots of time to do it on the pi. Once I wrote it all I just copied it over. I've been doing lots of Java is CSA so the switch to Python was nice, it's all much easier in my opinion, or at least simpler. 
## Calculator
### Description
In this assignment, we used functions to do an array of operations on two use inputted numbers. I'd never used functions in Python before so this was a fun challenge. 
### Code
I'm going to talk about the two sections that gave me the most trouble. The first is taking the input from a function. 
`calculator.py`
```python 
print("Sum:\t\t" , doMath(a,b,1))
```
There a few parts to this. First, the print, we are really just telling python to print "Sum" and the return from doMath. The second big part is giving doMath its arguments, in this case, that is `a,b,1` a, and b are variable that are given their value by a user input earlier in the code. 1 is telling doMath what operation to do.  

Next is how I chose what operation to do.
`calculator.py`
```python
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
 ```
C is the argument from the earlier print, it has a value of 1-5 at all times. Because of this we can use this simple solution, every value of c has an if/if else statment. The program finds the correct operation, completes it, and then returns it to be printed. 
### Lessons(s) Learned

- You can give a function values to work with (called an "argument"). You use `return` to spit back out the answer or whatever, not a `print`.
- Taking inputs is as easy as `x = input("Message")
- Rounding is very easy, just use `round(x,y)`, x being the number and y being the places to round to. 

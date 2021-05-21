# Engineering_4_Notebook
## Vann's Engineering 4 Stuff! :)
## Getting the Pi Online
I had to use a hotspot, set yours to 2.5 GHz under AP Band if, on android this took me a while to figure out the hard way.
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
## Quadratic Solver
### Description
In this assignment, we used functions with an array as the argument to solve a quadratic, or if no real roots exist, inform the user. 
### Code
`quadratic_solver`
```python 
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
```
This is where the (inefficient) magic happens. Outside of this all that happens is taking user-input and printing the result of this section. What I'm doing is just solving the quadratic formula while giving its value to one of the two roots. After getting both roots it rounds them and then returns the array to be printed. 
### Lessons(s) Learned
- Arrays can be useful when dealing with lots of similar variables, the individual elements are easy to manipulate and they keep code simple. 
- One main mistake I made was making the framework and then building the solver, had I done it the other way around my code would have been simpler and more efficient. 
- You can return an array and then print it along with other things just like a normal variable.  
## Strings and Loops
### Description
In this assignment, we asked the user for a phrase and then we spit it apart letter by letter and printed it out with a hyphen between the words.  
### Code
`strings_and_loops.py`
```python 
words = input("Enter the sentence: ").split(' ')   #takes the input from the user and puts it in a list with a space in between
for x in range(0, len(words)):  #a loop that runs for the length of the string
    for y in range(0,len(words[x])):  #loop that runs for the length 
        print(words[x][y])  #prints a letter from a part of the loop
    print("-")  #prints - in between words
```

This is the entire program; I'm going to go line by line an tak about what's happening. In line one we ask the user for an input phrase, the use the split function which makes it a list superated by the argument giving, in this case ' ', finally we set that to words. The next line is a for loop that runs once for every word in the phrase, this is done by giving it the range 0 to len(words). The next line is very similar, we are just looping through one time for every letter in the current word. One thing to note is the x and y. X is the current word in the list and y is the current letter in the list. Then we print out the letter, words gets two arguments, one is the word(x) and one is the letter(y). The final print statment for the hyphen is only in the first for loop so it only runs after every word, not every letter. 

### Lessons(s) Learned

- You can call an individual letter of a list.  
- For loops can take lots of different types of arguments. 
- Python can be very dense if written well or luckily(guess which I am ;). 
## Hangman
### Description
In this assignment, we made a hangman game, I modified mine to be single player.  
### Code
  Instead of chosing an individual segment of code I'm going to just talk about the differents parts as no part of the program is super complex. The section of the code is for defining variables and choosing the word. To choose the word the program picks a random word from the list and makes it it's own variable. In this section we also set the amount of lives. 
  The next section is the hangman function, this just takes an argument and then prints the correct hangman position. 
  The final section is the main functionality. A few things happen here, first we take a user guess. Then we check to see if they got it right, if the did we replace the underscore in the answer with the correct letter. IF they got it wrong they loose a life. Regardless of what happens we print the appropirate hangman position. Finally, after the user wins or loses, we tell them and end the program. 

### Lessons(s) Learned

- Large problems are really just a bunch of small problems. 
- Just making progress instead of looking at the bigger picture can help you deal with the scale of some problems. 
- I use to many variables. 
## GPIO #1
### Description
In this assignment, we blinked two LEDs ten times.   
### Code
   `bash`
```bash 
echo "Hello, World!" #print Hello, World!
gpio mode 0 out #setting the output pins
gpio mode 2 out

for (( x=0; x<=9; x++ ))  #loop that runs twice
  do  
  gpio write 0 1  #turn the leds on
  gpio write 2 1
  sleep 1         #wait one second
  gpio write 0 0  #turn them off
  gpio write 2 0
  sleep 1         #wait one second

done              #code finishes
```
The code is fairly simple, I just printed "Hello, World!" and then blinked the leds on and off ten times.  

### Lessons(s) Learned

- You should probably read linked pages
- Instead of trying to figure out what pins are associated to the number in the code, just hook up and led to ground and tap each pin to find which one works. 
- Bash scripts aren't that involved
## Python Pins
### Description
In this assignment, we blinked an LED using Python.   
### Code
   `python`
```python_pins.py
for x in range(10):   #loop runs 10 times
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
```
I just wrote a for loop that repeats 10 times. I found the code for the LEDS [here](https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/).  

### Lessons(s) Learned

- Sometimes you can just google the problem and get lucky!
- Past notebooks can come in handy! 
- Using the transmit/recive pins to blink an LED works but also seems to disconnect me...

## SSH
### Description
In this assignment, we connected to our pi via SSH and turned on an LED. 
### How
I followed Shields' tutorial until it cam time to connect to the pi. I tried his chromebook method but didn't have any luck so I used an app on my android called "JuiceSSH - SSH Client". I'm not sure if it's the best but it worked first try. To connect I entered "pi@192.168.43.31:22" pi was my username, 192... was my ip, and 22 was my port (default). To get power to the pi I connected the battery to the boost thing and then used the usb port on the boost and the micro usb on the pi to get power. I also used pin 17 as my led pin. 
### Lessons(s) Learned
- Connecting via SSH is simple (not always easy).
- The pi's ip seems to be static or at least does not change every reboot. 
- I really don't want to be a network engineer. 
## I2C
### Description
In this assignment, we printed accelerometer data on a display. 
### How
I primarily used the tutorial Shields had on the page, it was very good and got me 90% of the way to working hardware. I had one issue that gave me lots of grief. I'm not sure what cause it but I could never get shapes.py to run without errors, I think I uncommented/left something commented that I should not have but it would never run. Eventually I used Gram Lenard's code and it worked first try. I belive this is because his code was slimmed down and only had what we needed for our rig. Regadless there would have been a lot more head scratching if he hadn't posted his code. 
### Lessons(s) Learned
- The Pi can throw errors if wiring is wrong so checking wiring is something I have to do now even with code errors. 
- These displays seems to be tricky regardless of language or other hardware. 

## Hello Flask
### Description
In this assignment, we turned the pi into a web-server. 
### How
This assignment was suprisingly smooth, I followed the tutorial and everything worked. MY largest takeaway is that I have to be on the same network as my pi for it to work, that means I had to connect to my phone hotspot to get acess to the webpage. 
### Lessons(s) Learned
- Follow the tutorial as long as it works.
- You have to be on the same network to connect to the pi. 

## Pi Camera
### Description 
In this assignment we usedthe pi camera to take pictures with effects. 
### How
I followed the docs and everything went well. One thing to note is that the gold contacts face down on the pi and up twoards the camera on the camera. 
### Code
 `python`
```camera_test02.py
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'colorswap' #this is where you put the code for the effect   
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test1.jpg')

```
The only thing I'd like to point out with the code is where you put the image effect function thing. I put it after the resolution but before the preview and it worked fine. There is a list of the effects in the doc. 
### Lessons(s) Learned
- Follow the docs, they get you like 90% of the way there
- Use "git add ." to add multiple files
## Headless
### Description 
In this assignment we graphed acceleration data on the screen and and then sshd in. 
### How
I had SSH figured out so it wasn't a big deal. 
### Lessons(s) Learned
- Follow the docs, they get you like 90% of the way there
- The top left of the screen is (0,0)
## GPIO Flask
### Description 
In this assignment we used a web server to control LEDs. 
### How
Philip helped me set up the web server for our project so whereas I never actually got the leds working I did use a servo which I think counts. 
### Lessons(s) Learned
- You can use discord image links instead of file paths for images. 
- Spacing is really important in Python. 
## CopyPasta 1 & 2
### Description 

import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24  #RST Pin
accelerometer = Adafruit_LSM303.LSM303() # accelerometer setup
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) # dislay setup
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) # gets drwaing object to draw on image
draw.rectangle((0,0,width,height), outline=0, fill=0) # clears screen

#variables for drawing
padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default() 

#Everything above this was in the examples

while True:   #runs the whole time
	accel, mag = accelerometer.read() # gets accelerometer data
	accel_x, accel_y, accel_z = accel #sets the acceleration values
	#mag_x, mag_y, mag_z = mag #I dont print these values but good to have
	
	#prepares the drawing on the screen
	#(0,0) is the top left. Increasing each number goes right/down
	#using .format (from the examples), and divided the value by 100, then rounded to 3 places
	draw.text((x, top), "Accelerometer Data:", font=font, fill=255) # draws header
	draw.text((x, top + 10), "Accel x ={0}".format(round(accel_x / 100, 3)), font=font, fill=255) # prints x 
	draw.text((x, top + 20), "Accel y ={0}".format(round(accel_y / 100, 3)), font=font, fill=255) # prints y
	draw.text((x, top + 30), "Accel z ={0}".format(round(accel_z / 100, 3)), font=font, fill=255) # prints z
	
	#these lines do the printing
	disp.image(image) # displays x, y, z, and header
	disp.display()

	#prepares and writes over the place where the accelerometer values are, essentially clearing the screen there
	draw.rectangle((100, 12, 55, 50), outline=0, fill=0) # "refreshes" the xyz values so they can be updated
	disp.image(image)
	disp.display()

	#sleep for debug, I've found it to be useful in the past
	time.sleep(.15)


import time
import Adafruit_SSD1306
import Adafruit_LSM303
import math

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
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

# variables to help drawing
padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default()

x_Changer = 0

while True:

	#this moves the x value of the point printed along the screen
	x_Value = x + x_Changer


	accel, mag = accelerometer.read() # gets accelerometer data
	accel_x, accel_y, accel_z = accel #sets the acceleration values
	mag_x, mag_y, mag_z = mag 
	

	# this maps the value of the accel_x to a point on the OLED Screen
	dataValue = abs(accel_x/10)
	#if the dataValue would interfere with the heading visually, then put in below the heading
	if dataValue <= 3:
		dataValue = 3
	#prints the value so you can see the actual number on the pi
	print(dataValue)



	draw.text((x, top), "Accel Data:", font=font, fill=255) # draws header
	#draws a . where you want it to be
	# it (.) moves 1 px over every iteration
	#and moves up/down the screen depending on the accel values
	draw.text((x_Value, top + dataValue),".", font=font, fill=255) 


	#actually writes to the display
	disp.image(image) # displays x, y, z, and header
	disp.display()

	
	x_Changer = x_Changer + 1 #moves the x value of the . one over; iteration complete

	time.sleep(.1) #debug


# To run this code in Python I use a plugin called Pillow

#Download an image from the internet and save it to your hard drive
#In Python, run the following code:

from PIL import Image,ImageFilter
myImage = Image.open('C:\\Users\\lecky\\Downloads\\high tops sneakers.jpg')
myImage.load

#The syntax above will load the image. Now we can run several commands against it to get format and size, and even show the image

myImage.format
myImage.size
myImage.show()

# We can use the ImageFilter module to apply a filter to it and show it any way we like

blur = myImage.filter(ImageFilter(BLUR)).show()
quit()
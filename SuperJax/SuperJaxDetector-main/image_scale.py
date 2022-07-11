from PIL import Image
import os

basewidth = 50

path = "/home/duhon/Documents/Code/Image Recognition/Mighty_Jax/"
pics = os.listdir(path)

for i in pics:
	img = Image.open(path + i)
	img = img.resize((basewidth, basewidth), Image.ANTIALIAS)
	img.save(i)


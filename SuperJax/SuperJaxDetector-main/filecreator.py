from PIL import Image
import os

path = "/home/duhon/Documents/Code/Image Recognition/Mighty_Jax/SuperJax/"
pics = os.listdir(path)

# for num, i in enumerate(pics):
# 	os.rename(path + i, f"bg{num}.png")

dimList = []

with open("jax.txt", "w") as f:
	for i in pics:
		im = Image.open(path + i)
		width, height = im.size
		buf = str(path + i + " 0")
		dimList.append(buf)
		# print(buf)
	for i in dimList:
		f.write(i + "\n")
	# print(dimList)

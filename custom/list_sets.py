import os

imgs = os.listdir("images/train")

for img in imgs:
	abso = os.path.abspath(img)
	with open("train.txt", "a+") as f:
		f.write(abso+'\n')
		f.close()
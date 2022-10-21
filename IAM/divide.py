import os
import shutil

with open("trainset.txt", "r") as f:
	trains = f.readlines()
	f.close()

images = []
for item in trains:
	item = item.split('-')[:-1]
	item = "-".join(item)+".png"
	images.append(item)

for img in images:
	try:
		print(img)
		origin = "IAM/"+img
		destin = "images/train/"+img
		shutil.move(origin, destin)
		print(img)
	except:
		a = 1
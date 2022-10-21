import os
import shutil

with open("train.txt", "r") as f:
	trains = f.readlines()
	f.close()

images = []
for item in trains:
	item = item.split('-')[:-1]
	item = "-".join(item)+".png"
	images.append(item)

for img in images:
	try:
		origin = "IAM/"+img
		destin = "images/train/"+img
		print(origin, destin)
		shutil.move(origin, destin)
		
	except:
		a = 1
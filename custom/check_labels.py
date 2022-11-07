import os
import cv2

sset = "train"
lista = os.listdir("labels/"+sset+"/")

for txt in lista:

	name = txt.split(".")[0]

	with open("labels/"+sset+"/"+txt) as f:
		lines = f.readlines()
		f.close()

	img = cv2.imread("images/"+sset+"/"+name+".png")
	height, width,_ = img.shape

	for li in lines:
		values = li.split()
		norm_xc = float(values[1])
		norm_yc = float(values[2])
		norm_w = float(values[3])
		norm_h = float(values[4])

		un_h = int(norm_h * height)
		un_w = int(norm_w * width)
		un_x = int((norm_xc *width) - (un_w/2))
		un_y = int((norm_yc * height) - (un_h/2))

		cv2.rectangle(img, (un_x, un_y), (un_x+un_w, un_y+un_h), (0, 0, 255), 6)

	resized = cv2.resize(img, (500,700))
	cv2.imshow("img", resized)
	cv2.waitKey(0)

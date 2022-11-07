import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET


prof = ['a01-020x', 'b02-013', 'c03-003e', 'e01-025','f03-174']

sset = "train" # train val
path = "images/"+sset+"/"
subset = os.listdir(path)

for t in subset:

	if ".gitkeep" in t:
		continue

	image = path+t
	img = cv2.imread(image)
	img_height = img.shape[0]
	img_width = img.shape[1]

	print(image)

	name = t.split("/")[-1][:-4]
	xml = "iamgt-xmls/"+name+".xml"

	file = "labels/"+sset+"/"+name+".txt"
	open(file, 'w+')

	tree = ET.parse(xml)
	root = tree.getroot()

	#file = "labels/"+set+"/"+name+".txt"
	#open(file, 'w+')

	squares = []
	for child in root[1]:
		try:
			for line in child:

				if len(line) == 1:
					attribs = line[0].attrib
					ponto_min = (int(attribs['x']), int(attribs['y']))
					ponto_max = (int(attribs['x']) + int(attribs['width']), int(attribs['y']) + int(attribs['height']))
					squares.append([ponto_min, ponto_max])
				else:
					x = []
					y = []
					for word in line:
						attribs = word.attrib
						x.append(int(attribs['x']))
						y.append(int(attribs['y']))
						x.append(int(attribs['x']) + int(attribs['width']))
						y.append(int(attribs['y']) + int(attribs['height']))
					ponto_min = (min(x), min(y))
					ponto_max = (max(x), max(y))
					squares.append([ponto_min, ponto_max])

		except:
			foo = 1

	for square in squares:
		x = square[0][0]
		y = square[0][1]
		width = square[1][0] - square[0][0]
		height  = square[1][1] - square[0][1]

		#img = cv2.rectangle(img, (x,y), (x+width, y+height), (0, 0, 255), 6)

		x += width/2
		y += height/2

		x = x/img_width
		y = y/img_height
		width = width/img_width
		height = height/img_height
		#print("0 "+str(x)+" "+str(y)+" "+str(width)+" "+str(height))
		#with open(file, "a+") as f:
		#	f.write("0 "+str(x)+" "+str(y)+" "+str(width)+" "+str(height)+"\n")
		#	f.close()

	#resized = cv2.resize(img, (500,700))
	#cv2.imshow("img", resized)
	#cv2.waitKey(0)


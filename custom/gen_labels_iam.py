import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET


#xmls = os.listdir("iamgt-xmls")

set = "val"
subset = []
for img in os.listdir("images/"+set):
	subset.append("images/"+set+"/"+img)

"""
train = []
for img in os.listdir("images/train"):
	train.append("images/train/"+img)

val = []
for img in os.listdir("images/val"):
	val.append("images/val/"+img)
"""


for t in val:

	img = cv2.imread(t)
	img_height = img.shape[0]
	img_width = img.shape[1]

	name = t.split("/")[-1][:-4]
	xml = "iamgt-xmls/"+name+".xml"

	tree = ET.parse(xml)
	root = tree.getroot()

	file = "labels/"+set+"/"+name+".txt"
	open(file, 'w+')


	linhas = []
	squares = []
	for child in root[1]:
		try:
			for line in child:
				"""
				for word in line:
					attribs = word.attrib
					ponto_min = (int(attribs['x']), int(attribs['y']))
					ponto_max = (int(attribs['x']) + int(attribs['width']), int(attribs['y']) + int(attribs['height']))
					squares.append([ponto_min, ponto_max])
				
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
				"""


				if len(line) == 1:
					attribs = line[0].attrib
					#ponto_min = (int(attribs['x']), int(attribs['y']))
					#ponto_max = (int(attribs['x']) + int(attribs['width']), int(attribs['y']) + int(attribs['height']))
					#squares.append([ponto_min, ponto_max])

					x = int(attribs['x'])
					y = int(attribs['y'])
					width = int(attribs['width'])
					height = int(attribs['height'])
					x += width/2
					y += height/2

					x = x/img_width
					y = y/img_height
					width = width/img_width
					height = height/img_height
					print("0 "+str(x)+" "+str(y)+" "+str(width)+" "+str(height))
					with open(file, "a+") as f:
						f.write("0 "+str(x)+" "+str(y)+" "+str(width)+" "+str(height)+"\n")
						f.close()
				else:
					"""
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
					"""
					for word in line:
						attribs = word.attrib
						x = int(attribs['x'])
						y = int(attribs['y'])
						width = int(attribs['width'])
						height = int(attribs['height'])
						x += width/2
						y += height/2

						x = x/img_width
						y = y/img_height
						width = width/img_width
						height = height/img_height
						print("0 "+str(x)+" "+str(y)+" "+str(width)+" "+str(height))
						with open(file, "a+") as f:
							f.write("0 "+str(x)+" "+str(y)+" "+str(width)+" "+str(height)+"\n")
							f.close()

		except:
			foo = 1
import os
import shutil
import argparse

# python divide.py --extension png

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--extension', type=str, default='png', help='Dataset Path')
	opt = parser.parse_args()

	ext = "."+opt.extension

	open('train.txt', 'w').close()
	open('val.txt', 'w').close()


	for img in os.listdir("./labels/train"):
		abso = os.path.abspath(img)
		abso = abso.split("/")[:-1]
		abso =  "/".join(abso)+"/images/train/"+img
		with open("train.txt", "a+") as f:
			f.write(abso+'\n')
			f.close()

	for img in os.listdir("./labels/val"):
		abso = os.path.abspath(img)
		abso = abso.split("/")[:-1]
		abso =  "/".join(abso)+"/images/val/"+img
		with open("val.txt", "a+") as f:
			f.write(abso+'\n')
			f.close()
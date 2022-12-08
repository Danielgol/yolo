import os
import shutil
import argparse

# python divide.py --dataset ./IAM --extension png

def read_data_with_subdirectorys(data_path, ext='.png'):
	path_list = []
	print("List of all directories in '% s':" % data_path)
	for path, subdirs, files in os.walk(data_path):
		for name in files:
			if name.endswith(ext):
				caminho = os.path.join(path, name).replace("\\", "/")
				#print(caminho)
				path_list.append(caminho)
	return path_list

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset', type=str, default='IAM', help='Dataset Path')
	parser.add_argument('--extension', type=str, default='png', help='Dataset Path')
	opt = parser.parse_args()

	ext = "."+opt.extension
	data_path = opt.dataset
	data_images = read_data_with_subdirectorys(data_path, ext)




	# Varia de acordo com o dataset ==============================================
	with open("trainset_iam.txt", "r") as f:
		trains = f.readlines()
		f.close()
	train_images = [] # todos os nomes das imagens de train (sem path)
	for item in trains:
		item = item.split('-')[:-1]
		item = "-".join(item)+ext
		train_images.append(item)

	with open("valset_iam.txt", "r") as f:
		vals = f.readlines()
		f.close()
	val_images = [] # todos os nomes das imagens de train (sem path)
	for item in vals:
		item = item.split('-')[:-1]
		item = "-".join(item)+ext
		val_images.append(item)

	with open("testset_iam.txt", "r") as f:
		tests = f.readlines()
		f.close()
	test_images = [] # todos os nomes das imagens de train (sem path)
	for item in tests:
		item = item.split('-')[:-1]
		item = "-".join(item)+ext
		test_images.append(item)
	# ============================================================================



	for img in data_images:
		name = img.split("/")[-1]
		if name in train_images:
			destin = "images/train/"+name
			print(img, destin)
			shutil.move(img, destin)

	for img in data_images:
		name = img.split("/")[-1]
		if name in val_images:
			destin = "images/val/"+name
			print(img, destin)
			shutil.move(img, destin)

	for img in data_images:
		name = img.split("/")[-1]
		if name in test_images:
			destin = "images/test/"+name
			print(img, destin)
			shutil.move(img, destin)



	# List sets =================================================================
	open('train.txt', 'w').close()
	imgs = os.listdir("images/train")
	for img in imgs:
		if ".gitkeep" in img:
			continue
		abso = os.path.abspath(img)
		abso = abso.split("/")[:-1]
		abso =  "/".join(abso)+"/images/train/"+img
		with open("train.txt", "a+") as f:
			f.write(abso+'\n')
			f.close()

	open('val.txt', 'w').close()
	imgs = os.listdir("images/val")
	for img in imgs:
		if ".gitkeep" in img:
			continue
		abso = os.path.abspath(img)
		abso = abso.split("/")[:-1]
		abso =  "/".join(abso)+"/images/val/"+img
		with open("val.txt", "a+") as f:
			f.write(abso+'\n')
			f.close()

	open('test.txt', 'w').close()
	imgs = os.listdir("images/test")
	for img in imgs:
		if ".gitkeep" in img:
			continue
		abso = os.path.abspath(img)
		abso = abso.split("/")[:-1]
		abso =  "/".join(abso)+"/images/test/"+img
		with open("test.txt", "a+") as f:
			f.write(abso+'\n')
			f.close()
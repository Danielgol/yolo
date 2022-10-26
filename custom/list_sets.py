import os

imgs = os.listdir("images/train")

for img in imgs:
        abso = os.path.abspath(img)
        abso = abso.split("/")[:-1]
        abso =  "/".join(abso)+"/images/train/"+img
        #print(abso)
        with open("train.txt", "a+") as f:
                f.write(abso+'\n')
                f.close()


imgs = os.listdir("images/val")

for img in imgs:
        abso = os.path.abspath(img)
        abso = abso.split("/")[:-1]
        abso =  "/".join(abso)+"/images/val/"+img
        #print(abso)
        with open("val.txt", "a+") as f:
                f.write(abso+'\n')
                f.close()
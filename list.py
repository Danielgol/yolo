import os

def read_data_with_subdirectorys(data_path, ext='.png'):
    path_list = []
    #print("List of all directories in '% s':" % data_path)
    for path, subdirs, files in os.walk(data_path):
        for name in files:
            if name.endswith(ext):
                path_list.append(os.path.join(path, name))

    return path_list


for img in read_data_with_subdirectorys("IAM"):
    print("./"+img.replace("\\", "/"))
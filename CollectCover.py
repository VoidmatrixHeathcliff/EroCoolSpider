import os
from shutil import copyfile

exists_files = os.listdir("Cover")

for folder in os.listdir("Gallery"):
    if folder + ".jpg" in exists_files:
        # print("Exists: " + folder + ".jpg")
        continue
    else:
        files = os.listdir("Gallery/" + folder)
        if "meta.json" in files:
            files.remove("meta.json")
            if len(files) > 0:
                # print("Copying " + folder + ".jpg ...")
                files.sort(key = lambda x:int(x[:-4]))
                copyfile("Gallery/" + folder + "/" + files[0], "Cover/" + folder + ".jpg")
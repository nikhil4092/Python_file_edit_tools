import os
import csv

def remove(name, path):
    for root, dirs, files in os.walk(path):
        for f in files:
            li = f.replace(name,"")
            print(li)
            os.rename(root + os.sep + f, root + os.sep + li)

remove('%20','./Sheets/bodyshop_all_images')
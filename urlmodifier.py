import os
import csv

def split(name, path):
    for root, dirs, files in os.walk(path):
        for f in files:
            li = f.partition(name)
            print(li[0]+li[1])
            os.rename(root + os.sep + f, root + os.sep + li[0]+li[1])

def csvrename(lines,split):
    j=0
    for i in lines:
    	li = lines[j][21].partition(split)
    	li2 = (li[0]+li[1]).rpartition('/')
        print(li2[-1])
        lines[j][21]=li2[-1]
        j+=1

#split('.jpg','./Sheets/parx_all_images')
#split('.png','./Sheets/parx_all_images')
#split('.JPG','./Sheets/parx_all_images')
#split('.jpeg','./Sheets/parx_all_images')
r = csv.reader(open('Sheets/vanheusen.csv')) # Here your csv file
lines = [l for l in r]
csvrename(lines,'.png')
csvrename(lines,'.jpg')
csvrename(lines,'.jpeg')
csvrename(lines,'.JPG')
with open('Sheets/vanheusen_clean.csv', 'ab') as a:                                    
    writer = csv.writer(a)                                                       
    writer.writerows(lines)

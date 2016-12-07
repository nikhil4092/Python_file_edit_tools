import csv
from collections import defaultdict
import os

def replace(name, path,i,lines,k):
    for root, dirs, files in os.walk(path):
        for f in files:
            if f==name:
            	os.rename(root + os.sep + f, root + os.sep + i)
            	lines[k][21]=i
            	break
columns = []
j=14143
k=0
r = csv.reader(open('./Sheets/vanheusen_clean.csv')) # Here your csv file
lines = [l for l in r]
for i in lines:
	replace(i[21],'./Sheets/vanheusen_all_images',`j`+".jpg",lines,k)
	#replace(i[21],'./Sheets/shoppersstop_all_images',`j`+".png",lines,k)
	#replace(i[21],'./Sheets/shoppersstop_all_images',`j`+".JPG",lines,k)
	#replace(i[21],'./Sheets/shoppersstop_all_images',`j`+".jpeg",lines,k)
	j+=1
	k+=1
with open('./Sheets/vanheusen_final.csv', 'ab') as a:                                    
    writer = csv.writer(a)                                                       
    writer.writerows(lines)
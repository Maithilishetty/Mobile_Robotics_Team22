
import csv
import os

dir = os.path.dirname(os.path.abspath(__file__))
img_file = os.path.join(dir, 'harbor_img_sequence_01.csv')
gt_file = open(os.path.join(dir, 'harbor_colmap_traj_sequence_01.txt'))
new_file = os.path.join(dir, "harbor01_GT.txt")

lines = gt_file.readlines() 
reader = csv.reader(open(img_file, 'r'))
d = {}
for row in reader:
   k, v = row
   d[v] = k
for line in lines:
    l = line.split()
    length = 6-len(l[0])+2
    l[0] = 'frame'+'0'*length+str(int(float(l[0])))+ '.png'
    if l[0] in d: 
        l[0] = d[l[0]]
    with open(new_file, 'a') as f:
        f.write(' '.join(str(i) for i in l))
        f.write('\n')
    




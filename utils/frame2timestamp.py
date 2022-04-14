import os
import csv

dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, 'harbor_img_sequence_07.csv')
with open(filename, 'r') as f:
    data_list = list(csv.reader(f))

with open(os.path.join(dir,'harbor07.txt'), 'w+') as f:
    for data in data_list:
        if data[1] != ' frame_id':
            f.write(data[0] + '\n')
            os.rename(os.path.join(dir, data[1]), os.path.join(dir, data[0] + '.png'))


import csv
import os 

path = os.path.abspath(os.getcwd())
path_to_csv_file = path + '/harbor_img_sequence_05.csv'
path_to_txt_file = path + '/timestamps.txt'
with open(path_to_txt_file, 'w') as f2:
    with open(path_to_csv_file, mode='r') as infile:
        reader = list(csv.reader(infile))  # load the whole file as a list
        header = reader[0]  # the first line is your header
        for row in reader[1:]:  # content is all the other lines
            f2.write(str(row[0])+'\n')  # writing line without last comma

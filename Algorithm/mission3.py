
import csv
file_path = ".\data-01-test-score.csv"
def read_file(file_path):
    data_list =[]
    f = open(file_path,'r',encoding='utf-8')
    csv_read = csv.reader(f)
    for line in csv_read:
        data_list.append(line)
    print(data_list)

read_file(file_path)
import csv

file_path = ".\data-01-test-score.csv"


class ReadCSV():

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self, data_list=[]):

        f = open(file_path, 'r', encoding='utf-8')
        csv_read = csv.reader(f)
        for line in csv_read:
            data_list.append(line)

    def merge_list(self, data_list,data_sum_list):
        for i in range(len(data_list)):
            data_sum_list.append(sum(map(int,data_list[i])))
        print(data_sum_list)
data_list = []
data_sum_list = []
e = ReadCSV(file_path)
e.read_file(data_list)
e.merge_list(data_list,data_sum_list)
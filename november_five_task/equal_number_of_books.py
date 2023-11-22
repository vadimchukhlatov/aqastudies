import csv
import json


class GetEqualNumberBooks:
    def __init__(self, json_file_name, csv_file_name):
        self.csv_file = self.get_csv_file(csv_file_name)
        self.json_file = self.get_json_file(json_file_name)
        self.result = self.give_equal_to_users()

    def get_csv_file(self, file_name):
        with open(file_name, newline='') as f:
            return [row for row in csv.DictReader(f)]

    def get_json_file(self, file_name):
        with open(file_name) as f:
            return json.load(f)

    def give_equal_to_users(self):
        avg = len(self.csv_file) / float(len(self.json_file))
        out = []
        last = 0.0
        while last < len(self.csv_file):
            out.append(self.csv_file[int(last):int(last + avg)])
            last += avg
        result = []
        for num, param in enumerate(self.json_file):
            result.append({'name': param['name'],
                           'gender': param['gender'],
                           'address': param['address'],
                           'age': param['age'],
                           'books': out[num]})
        return result

    def create_result_json(self):
        with open('result.json', 'w') as f:
            json.dump(self.result, f, indent=4)
        print('Файл успешно создан')

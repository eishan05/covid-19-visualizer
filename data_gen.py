import csv
import codecs

data_file = codecs.open('test_data.csv', 'rU', 'utf-16')
csv_file = csv.reader(data_file, delimiter=',')

data_file = open('country_code_maps.txt', 'w+')

country_code_map = {}
for row in csv_file:
  country_code_map[row[6]] = row[7]

for key in country_code_map:
  data_file.write(key + ': ' + country_code_map[key] + '\n')

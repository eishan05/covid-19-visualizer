from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row
import csv
import codecs

#Gets figure for a given country in the data list
def get_figure(country, data_list):
  z = [row[4] for row in data_list if row[6] == country]
  y = [None] * len(z)
  if len(z) > 0:
    y[0] = int(z[0])
  for i in range(1, len(y)):
    y[i] = y[i-1] + int(z[i])
  x = [i for i in range(len(y))]
  # create a new plot with a title and axis labels
  p = figure(title="Number of cases in " + country, x_axis_label='days', y_axis_label='number of cases')
  # add a line renderer with legend and line thickness
  p.line(x, y, legend_label="", line_width=2)
  p.legend.visible = False
  return p

#open csv file with COVID-19 data
data_file = codecs.open('test_data.csv', 'rU', 'utf-16')
csv_file = csv.reader(data_file, delimiter=',')

country = raw_input("What file name (without extension type): ")
# output to static HTML file
out_name = country + '.html'
output_file(out_name)
data_list = list(csv_file)
data_list.reverse();
country_set = set();
count = 0
for i in range(0, len(data_list) - 1):
  country_set.add(data_list[i][6])
print "Loading ... "
figure_list = []
count = 0
#for county in country_set:
#  if county == 'Canada' or county == 'United_States_of_America' or county == 'China' or county == 'South_Korea': 
#    figure_list.append(get_figure(county, data_list))
# show the results
show(row(column(get_figure('United_States_of_America', data_list), get_figure('Canada', data_list)), column(get_figure('China', data_list), get_figure('South_Korea', data_list)), column(get_figure('India', data_list), get_figure('Italy', data_list))))

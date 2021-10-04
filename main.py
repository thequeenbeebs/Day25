# WORKING WITH CSV DATA AND THE PANDAS LIBRARY

# CSV - Comma Separated Values (spreadsheets, etc - a way to represent tabular data)

# with open('weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Pandas - Python data analysis library w/ two structures
#   DataFrame - whole table
#   Series - equivalent to a list, a single column in the table


import pandas

# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temps = data['temp']
# print(temps.mean())

# print(temps.max())

# Get Data in Columns
# print(data['condition'])
# print(data.condition)

# # Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# print(int(monday.temp) * 9 / 5 + 32)

# # Create a dataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey = data[data['Primary Fur Color'] == 'Gray']
grey_count = len(grey)
red = data[data['Primary Fur Color'] == 'Cinnamon']
red_count = len(red)
black = data[data['Primary Fur Color'] == 'Black']
black_count = len(black)

squirrel_count = {
    "Fur Color": ['grey', 'red', 'black'],
    "Count": [grey_count, red_count, black_count]
}

new_data = pandas.DataFrame(squirrel_count)
new_data.to_csv('squirrel_count.csv')





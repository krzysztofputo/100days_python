import csv

# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

data_csv = pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")



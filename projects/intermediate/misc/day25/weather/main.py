# Import csv
import csv
import pandas as pd
csv_file = "weather_data.csv"


with open(csv_file) as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))
    
    print(temp)

df = pd.read_csv(csv_file)
print(df["temp"])
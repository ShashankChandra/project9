import csv
import pandas as pd
import statistics

with open("SOCR-HeightWeight.csv", newline = "") as file_open:
  reader = csv.reader(file_open)
  file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
  n_num = file_data[i][2]
  new_data.append(float(n_num))

mean = statistics.mean(new_data)
median = statistics.median(new_data)
mode = statistics.mode(new_data)

print("Mean: " , mean)
print("Median: " , median)
print("Mode: " , mode)

import csv

with open("FC_Log.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([1,2,3,4,5,6,7])

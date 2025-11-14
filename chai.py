'''import csv,tabulate as t,time
print('DECEMBER CHAI CONSUMED')
ch=open('E:\chai\chai.csv','r')
w=csv.reader(ch)
for i in w:
    print(i)
ch.close()'''

import csv
from tabulate import tabulate
from datetime import datetime

print("=== CHAI TRACKER ===\n")

csv_path = r"E:\chai\chai.csv"

try:
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    # create CSV if not found
    data = [["Date", "Cups"]]


print("Previous Records:\n")
print(tabulate(data[1:], headers=data[0], tablefmt="grid"))


cups = input("\nHow many cups of chai did you drink today? ")

try:
    cups = int(cups)
except:
    print("Invalid number. Using 0.")
    cups = 0

# Today's date/ however your format goes
today = datetime.now().strftime("%Y-%m-%d")


data.append([today, cups])

# Saving the csv
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("\n✔ Saved!")
print("\nUpdated Records:\n")
print(tabulate(data[1:], headers=data[0], tablefmt="grid"))


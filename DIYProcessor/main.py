import json
import csv
import os

fileName = dict()

folder = "Spreadsheet"

for filename in os.listdir(folder):
    with open("Spreadsheet/{}".format(filename), 'r') as file:
        reader = csv.DictReader(file, dialect=csv.excel)
        for row in reader:
            if "Filename" not in list(row.keys()):
                break
            if row["Name"] in fileName:
                fileName[row["Name"]].append(row["Filename"])
            else:
                fileName[row["Name"]] = [row["Filename"]]
print(fileName)
diyList = {}
with open("Recipes.csv", 'r') as DIY_CSV:
    reader = csv.DictReader(DIY_CSV, dialect=csv.excel)
    for row in reader:
        material = {}
        for x in range(6):
            y = x + 1
            if row["#{}".format(y)] != "":
                material[row["Material {}".format(y)]] = int(row["#{}".format(y)])
            else:
                break
        image = "https://acnhcdn.com/latest/FtrIcon/{}.png".format(fileName[row["Name"]][0])
        diyList[row["Name"].title()] = {"materials": material, 'sell': row["Sell"], "buy": row["Buy"],
                   "miles": row["Miles Price"], "Unlock": row["Recipes to Unlock"], "added": row["Version Added"],
                   "unlocked": row["Version Unlocked"], 'source': row["Source"], "category": row["Category"],
                   'EntryID': row["Unique Entry ID"], "image": image}

with open('result.json', 'w') as fp:
    json.dump(diyList, fp, indent=4)


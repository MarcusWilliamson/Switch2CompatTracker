import csv
import json

files = [("assets/progress_issues.csv", "Progress issues"), ("assets/updated.csv", "Updated")]
data = []

# Attempts to convert game title to eshop url
def get_url(title):
    t = str.maketrans(" .[:", "----", "]~!?/'#*")  # happy pride
    return ("https://www.nintendo.com/us/store/products/" + title.lower().replace(' - ', '-')
            .replace('&', 'and').translate(t)#.replace('.','-').replace('[', '-')
            .replace('+', '-plus') + "-switch").replace('--', '-')

# Read from the csv file and convert to a dictionary
def generate(filename, group):
    newData = []
    fields = []

    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="|")
        fields = next(csv_reader)

        for row in csv_reader:
            title, publisher = row[0], row[1]
            title = title.lstrip()
            publisher = publisher.rstrip()

            d = {fields[0]: title, fields[1]: publisher, "url":get_url(title), "group": group}
            newData.append(d)
    csv_file.close()
    return newData

def main():
    data = []
    for file in files:
        data += generate(file[0], file[1])
            
    with open("../src/json/game_list.json", 'w') as json_file:
        json.dump(data, json_file, indent=2)
    json_file.close()
    print("Done")


if __name__ == "__main__":
    main()
import csv
import json

files = [("assets/startup_issues.csv", "Startup issues"), ("assets/in-game_issues.csv", "In-game issues")]
data = []

def get_url(title):
    t = str.maketrans(" ", "-", ":]~!?/.'")  # happy pride
    return ("https://www.nintendo.com/us/store/products/" + title.lower().replace(' - ', '-')
            .replace('&', 'and').translate(t).replace('[', '-').replace('--', '-') + "-switch")

def generate(filename, group):
    newData = []
    fields = []

    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
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
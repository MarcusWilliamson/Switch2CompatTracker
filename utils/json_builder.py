import csv
import json

filename = "../src/csv/startup_issues.csv"

def get_url(title):
    # return ("https://www.nintendo.com/us/store/products/" + title.lower().replace(" ", "-").replace(":", "")
    #        .replace("[","").replace("]","").replace("~","") + "-switch")

    t = str.maketrans(" ", "-", ":[]~!?")  # happy pride
    return "https://www.nintendo.com/us/store/products/" + title.lower().translate(t) + "-switch"

def main():
    data = []
    fields = []

    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)

        fields = next(csv_reader)

        for row in csv_reader:
            title, publisher = row[0], row[1]
            title = title.lstrip()
            publisher = publisher.rstrip()

            d = {fields[0]: title, fields[1]: publisher, "url":get_url(title)}
            data.append(d)
            
    with open("startup_issues.json", 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == "__main__":
    main()
import csv

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
            
    for d in data:
        print (d)


if __name__ == "__main__":
    main()
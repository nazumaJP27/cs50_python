import sys
import csv


def main():
    get_2argvs()
    outputF_csv(sys.argv[1], sys.argv[2])


def get_2argvs():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1][-4:] or ".csv" not in sys.argv[2][-4:]:
        sys.exit("Not a CSV file")
    return sys.argv[1], sys.argv[2]


def outputF_csv(csv_in, csv_out):
    before = csv_in
    after = csv_out
    try:
        fmt_dicts = [] # A new list of dicts formated with keys: "first","second","house"
        with open(before, "r", newline="") as file:
            reader = csv.DictReader(file)
            dicts = []
            for row in reader:
                dicts.append(row)
            for dict in dicts:
                last, first = dict["name"].split(",")
                house = dict["house"]
                dict = {"first": first.strip(), "last": last, "house": house}
                fmt_dicts.append(dict)

        '''fmt_dicts = sorted(fmt_dicts, key=lambda dict: dict["first"])'''

        with open(after, "w", newline='') as file:
            write = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            write.writeheader()

            '''for row in fmt_dicts:
                write.writerow({"first": row['first'], "last": row['last'], "house": row['house']})'''

            write.writerows(fmt_dicts)
    except FileNotFoundError:
        sys.exit("Table does not exist")


if __name__ == "__main__":
    main()

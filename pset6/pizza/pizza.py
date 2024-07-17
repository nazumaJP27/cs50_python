import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1][-4:]:
        sys.exit("Not a CSV file")

    table = sys.argv[1]
    menu = []

    try:
        with open(table, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)

        print(tabulate(menu, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("Table does not exist")


if __name__ == "__main__":
    main()

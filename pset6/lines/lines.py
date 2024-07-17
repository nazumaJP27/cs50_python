import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1][-3:]:
        sys.exit("Not a Python file")

    file_path = sys.argv[1]
    lines = 0

    try:
        with open(file_path, "r") as file:
            for row in file:
                line = 0
                if row.lstrip().startswith("#") == False and row.isspace() == False:
                    lines += 1

            print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

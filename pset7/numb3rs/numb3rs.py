import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if matches:
        groups = list(matches.group(1,2,3,4))
        print(groups)
        for group in groups:
            if len(group) > 3:
                print(len(group))
                return False
            elif not (0 <= int(group) <= 255):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()

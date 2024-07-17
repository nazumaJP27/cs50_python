import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"([\d|:]+ [a-z]+) to ([\d|:]+ [a-z]+)", s, re.IGNORECASE):
        matches = matches.groups()
        in_work, out_work = matches
        in_work = in_work.split()
        out_work = out_work.split()
        in_work = {"hour": in_work[0], "ampm": in_work[1]}
        out_work = {"hour": out_work[0], "ampm": out_work[1]}

        if ":" in (in_work["hour"]) and validate_hour(in_work["hour"]) == True:
            in_work["hour"] = in_work["hour"].split(":")
            in_hour = [int(in_work["hour"][0]), int(in_work["hour"][1])]
        elif ":" not in (in_work["hour"]):
            in_hour = [int(in_work["hour"]), 0]

        if ":" in (out_work["hour"]) and validate_hour(out_work["hour"]) == True:
            out_work["hour"] = out_work["hour"].split(":")
            out_hour = [int(out_work["hour"][0]), int(out_work["hour"][1])]
        elif ":" not in (out_work["hour"]):
            out_hour = [int(out_work["hour"]), 0]

        else:
            raise ValueError

        if in_hour[0] == 12:
            in_hour[0] = 0

        if out_hour[0] == 12:
            out_hour[0] = 0

        if in_work["ampm"].upper() == "PM":
            in_hour = [in_hour[0] + 12, in_hour[1]]
        elif out_work["ampm"].upper() == "PM":
            out_hour = [out_hour[0] + 12, out_hour[1]]

        return f"{in_hour[0]:02}:{in_hour[1]:02} to {out_hour[0]:02}:{out_hour[1]:02}"

    else:
        raise ValueError


def validate_hour(s):
    h, min = s.split(":")
    h, min = map(int, (h, min))
    if 0 <= min <= 59 and 1 <= h <= 12:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

''' This program converts any dates typed in the format used in the US (middle-endian),
and outputs the correspondent date in ISO 8601, an international standard that prescribes
that dates should be formatted in year-month-day (YYYY-MM-DD) order
'''

def main():
    date = get_middleEndian_date() #This function will return a list of 3 int (month, day, year)
    print(f"{date[2]:04}-{date[0]:02}-{date[1]:02}")


def get_middleEndian_date():
    months = [ 0,
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        date = input("Date: ").strip().title()
        try:
            if date.find("/") > 0:
                m, d, y = date.split("/")
                len_y = len(y)
                m, d, y = int(m), int(d), int(y)
            elif date.find(",") > 0:
                m, d, y = date.split(" ")
                len_y = len(y)
                d, m, y = int(d.strip(",")), int(months.index(m)), int(y)
            else:
                continue
        except (NameError, ValueError):
            continue
        if 1 <= d <= 31 and 1 <= m <= 12 and 0 <= y and len_y == 4:
            break
        else:
            continue
    return m, d, y


def first_implementation():
    months = [ 0,
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        prompt = input("Date: ").strip().title()
        try:
            if prompt.find("/") > 0:
                m, d, y = prompt.split("/")
                m = int(m)
                d = int(d)
            else:
                m, d, y = prompt.split(" ")
                d = int(d.strip(","))
                m = int(months.index(m))
        except (NameError, ValueError):
            continue
        if d <= 31 | m <= 12 | len(y) == 3:
            break
        else:
            continue
    print(f"{y}-{m:02}-{d:02}")


main()

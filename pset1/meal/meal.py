def main():
    h = input("What time is it? ").strip()
    meal = round(convert(h))

    match meal:
        case 7 | 8:
            print("breakfast time")
        case 12 | 13:
            print("lunch time")
        case 18 | 19:
            print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    min = int(minutes) / 60
    h = int(hours)
    return float(h + min)

if __name__ == "__main__":
    main()


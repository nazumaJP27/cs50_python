def main():
    while True:
        try:
            fraction = input()
            if "/" in fraction:
                percentage = convert(fraction)
                if 0 <= percentage <= 100:
                    break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")

    if x.isnumeric() == False or y.isnumeric() == False:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    else:
        x, y = int(x), int(y)
        z = round((x / y) * 100)
        return z


def gauge(percentage):
    match percentage:
        case _ if 1 < percentage < 99:
            return f"{percentage}%"
        case _ if percentage <= 1:
            return "E"
        case _ if percentage >= 99:
            return "F"


if __name__ == "__main__":
    main()

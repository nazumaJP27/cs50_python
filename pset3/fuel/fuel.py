# Output the percentage of a fraction

def main():
    x = fraction("Fraction: ")

    match x:
        case _ if 1 < x < 99:
            print(f"{x}%")
        case _ if x <= 1:
            print("E")
        case _ if x >= 99:
            print("F")


def fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x, y = int(x), int(y)
            z = round((x / y) * 100)
            if z > 100:
                continue
            return z
        except (ValueError, ZeroDivisionError):
            pass


main()



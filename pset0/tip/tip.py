def main():
    dollars = dollars_to_float(input("How much was the meal? ").lstrip("$"))
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip("%"))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    x = float(d)
    return x


def percent_to_float(p):
    y = float(p)
    return y / 100



main()
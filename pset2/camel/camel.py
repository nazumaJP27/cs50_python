def main():
    camel = input("camelCase name: ").strip()
    snake_case(camel)


def snake_case(s):
    for c in s:
        l = c.islower()
        if l == True:
            print(c, end="")
        else:
            print(f"_{c.lower()}", end="")
    print()


main()

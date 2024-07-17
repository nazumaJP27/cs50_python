def main():
    str = input("Input: ").strip()
    no_vowel(str)
    print()


def no_vowel(s):
    for c in s:
        l = is_vowel(c)
        if l == None:
            print(c, end="")
        else:
            print("", end="")


def is_vowel(c):
    x = c.lower()
    match x:
        case "a" | "e" | "i" | "o" | "u":
            return True


main()

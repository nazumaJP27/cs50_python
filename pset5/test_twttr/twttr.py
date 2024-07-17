def main():
    str = input("Input: ").strip()
    print(shorten(str))


def is_vowel(char):
    x = char.lower()
    match x:
        case "a" | "e" | "i" | "o" | "u":
            return True
    return False


def shorten(word):
    for char in word:
        if is_vowel(char) == True:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()

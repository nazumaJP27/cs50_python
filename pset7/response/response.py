from validator_collection import validators, checkers, errors


def main():
    print(validator(input("What's your email address? ")))


def validator(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()

def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Chek if str contain a maximum of 6 chars
    def in_length(n):
        if 2 <= n <= 6:
            return True
        else:
            return False


    def num_betw(s):
        def has_num(s):
            for char in s:
                if char.isnumeric():
                    return True
            return False

        def has_alpha(s):
            for char in s:
                if char.isalpha():
                    return True
            return False


        if s[-1].isalpha() and has_num(s):
            return True

        if s[-1].isnumeric() and has_alpha(s) and s[0].isnumeric():
            return True

        return False

# Check if input is valid
    chars = len(s)
    x = s[0:2]
    y = s[2:len(s)]


    if in_length(chars) == True:
        if x.isalpha() == True:
            if "0" in y[0]:
                return False
            if y.isalnum() == True:
                if num_betw(y) == True:
                    return False
                return True
        else:
            return False

if __name__ == "__main__":
    main()


'''
def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

# Chek if str contain a maximum of 6 chars
    def in_length(n):
        if 2 <= n <= 6:
            return True
        else:
            return False


    def num_betw(s):
        def has_num(s):
            for char in s:
                if char.isnumeric():
                    return True
            return False

        def has_alpha(s):
            for char in s:
                if char.isalpha():
                    return True
            return False


        if s[-1].isalpha() and has_num(s):
            return True

        if s[-1].isnumeric() and has_alpha(s) and s[0].isnumeric():
            return True

        return False

# Check if input is valid
    chars = len(s)
    x = s[0:2]
    y = s[2:len(s)]


    if in_length(chars) == True:
        if x.isalpha() == True:
            if "0" in y[0]:
                return False
            if y.isalnum() == True:
                if num_betw(y) == True:
                    return False
                return True


main()
'''

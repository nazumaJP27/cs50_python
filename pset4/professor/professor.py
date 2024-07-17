''' The program asks the user for a level; then gives 10 math problems to solve;
    output the score.'''

import random

def main():
    score = 0
    level = get_level() # Asks for level 1 to 3

    for _ in range(10):
        x = generate_integer(level) # Gets a random integer based on the level:
        y = generate_integer(level) # 1 = one digit, 2 = two...

        print(f"{x} + {y} =", end=" ")

        z = input()
        if z.isdigit() == False or int(z) != (x + y):
            print("EEE")
            for _ in range(2):
                print(f"{x} + {y} =", end=" ")
                try:
                    z = int(input())
                    if z != (x + y):
                        print("EEE")
                    else:
                        break
                except ValueError:
                    print("EEE")
            if z != (x + y):
                print(f"{x} + {y} = {x + y}")
        else:
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        num_d = [0, 9]
    elif level == 2:
        num_d = [10, 99]
    elif level == 3:
        num_d = [100, 999]
    else:
        raise ValueError

    n = random.randint(num_d[0], num_d[1])
    return n


if __name__ == "__main__":
    main()

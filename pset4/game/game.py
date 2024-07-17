def get_list_numbers(prompt):
    numbers = []
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                for i in range(1, n + 1):
                    numbers += [i]
                return numbers
        except ValueError:
            pass


def main():
    import random

    numbers = get_list_numbers("Level: ")
    number = random.choice(numbers)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess == number:
                print("Just right!")
                break
            elif guess < number:
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            pass

if __name__ == "__main__":
    main()

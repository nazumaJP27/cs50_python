def main():
    # Set amount due
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        x = get_coin()
        amount = amount - x

    change = - amount
    print(f"Change Owed: {change}")


def get_coin():
    x = int(input("Insert Coin: "))
    if x == 25:
        return x
    elif x == 10:
        return x
    elif x == 5:
        return x
    return 0


main()

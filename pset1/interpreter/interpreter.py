def main():

# Assign a value to i, y, j
    i, y, j = input("Expression: ").strip().split(" ")
    x = int(i)
    z = int(j)

# Convert to float and output the result
    result = cal(y, x, z)
    print(float(result))

# Calculate the two values based of the opearator y
def cal(y, x, z):
    match y:
        case "+":
            return(x + z)
        case "-":
            return(x - z)
        case "*":
            return(x * z)
        case "/":
            return(x / z)


main()

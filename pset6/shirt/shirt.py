import sys
from PIL import Image, ImageOps


def main():
    get_2argvs()
    shirt = Image.open("shirt.png")
    size = shirt.size

    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    image = ImageOps.fit(image, size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])


def get_2argvs():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    formats = ["jpg", "jpeg", "png"]
    if sys.argv[1].split(".")[1] not in formats or sys.argv[2].split(".")[1] not in formats:
        sys.exit("Invalid input")
    inputF = sys.argv[1].split(".")[1]
    outputF = sys.argv[2].split(".")[1]
    if inputF != outputF:
        sys.exit("Input and output have different extensions")
    return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()

from pyfiglet import Figlet
import sys
import random

f = Figlet()
fonts = f.getFonts()
font = random.choice(fonts)

try:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    elif sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        font = sys.argv[2]
except IndexError:
    pass

figlet = Figlet(font=font)
prompt = input("Input: ")

print(f"Output in {font}:")
print(figlet.renderText(prompt))

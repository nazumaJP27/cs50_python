import inflect

p = inflect.engine()

names = []

while True:
    try:
        prompt = input("Name: ").strip().title()
        names += [prompt]
        print(names)
    except EOFError:
        names = p.join((names))
        print(names)
        print(f"Adieu, adieu, to", names)
        break
    except ValueError:
        pass

#

#

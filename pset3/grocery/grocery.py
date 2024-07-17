g_dict = {}

while True:
    try:
        key = input().strip().upper()
        if key in g_dict:
            g_dict[key] += 1
        else:
            g_dict[key] = 1

    except EOFError:
        g_dict = dict(sorted(g_dict.items()))
        for item in g_dict:
            print(g_dict[item], item)
        break
    except (KeyError, ValueError):
        pass



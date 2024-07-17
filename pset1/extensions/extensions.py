def main():

    file = input("File name: ").strip().lower()

    if file.find(".") < 0:
        print("application/octet-stream")
    else:
        ext(file)

def ext(s):

    x, y = s.rsplit(".", 1)

    match y:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "gif" | "png":
            print(f"image/{y}")
        case "pdf" | "zip":
            print(f"application/{y}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


main()

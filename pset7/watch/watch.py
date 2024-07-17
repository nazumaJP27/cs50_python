import re
import sys


def main():
    print(parse(input("HTML: ").strip()))
    

'''<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'''
def parse(s):
    matches = re.search(r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([\w?=-]+)".*?>', s)
    if matches:
        url = "https://youtu.be/"
        youBe = matches.group(1)
        return url + youBe


if __name__ == "__main__":
    main()

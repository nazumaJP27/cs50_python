'''implement a program that prompts the user for their date of birth in YYYY-MM-DD format
and then prints how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals, just like the song from Rent, without any and between words.
Since a user might not know the time at which they were born, assume, for simplicity,
that the user was born at midnight (i.e., 00:00:00) on that date.
And assume that the current time is also midnight. In other words,
even if the user runs the program at noon, assume that it’s actually midnight, on the same date.'''


import inflect
p = inflect.engine()
import sys
from datetime import date



class Dates:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    @classmethod
    def getBirth(cls):
        try:
            birthDate = input("Date of Birth: ")
            y, m, d = map(int, birthDate.split("-"))
            return cls(y, m, d)
        except ValueError:
            sys.exit("Invalid date")

    def daysPassed(self):
        today = date.today()
        birth = date(self.y, self.m, self.d)
        passed = today - birth
        return passed.days

    def minutesPassed(self):
        minutes = self.daysPassed() * 24 * 60
        return minutes

    def minutesOld(self):
        return p.number_to_words(self.minutesPassed(), andword="")


def main():
    print(date.today())
    birth = Dates.getBirth()
    print(birth.minutesOld().capitalize(), "minutes")






if __name__ == "__main__":
    main()

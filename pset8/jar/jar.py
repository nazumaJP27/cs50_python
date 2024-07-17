class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookie_emoji = "🍪"
        cookies = cookie_emoji * self.size
        return f"{cookies}"
        return f"{self.size}/{self.capacity}"

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError
        return self._size

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

if __name__ == "__main__":
    jar = Jar()
    jar.deposit(int(input("Deposit how many cookies? ")))
    jar.withdraw(int(input("Withdraw how many cookies? ")))
    print(jar)



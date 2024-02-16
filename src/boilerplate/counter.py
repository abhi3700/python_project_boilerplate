class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0


def main():
    """
    Purpose: Test counter
    """

    c = Counter()
    c.increment()
    c.increment()
    c.increment()

    print(f"After incrementing 3 times, value: {c.count}")
    c.reset()

    print(f"After reset, value: {c.count}")


# end def

if __name__ == "__main__":
    main()

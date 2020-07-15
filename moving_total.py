class MovingTotal:

    def __init__(self):
        self.numbers = []
        self.totals = set()

    def append(self, numbers):
        self.numbers = self.numbers + numbers
        self.numbers = self.numbers[-3:]
        self.totals.add(sum(self.numbers))

    def contains(self, total):
        if total in self.totals:
            return True
        else:
            return False
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    print(movingtotal.contains(6))

    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))

    movingtotal.append([4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(7))
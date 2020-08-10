class Stairs:
    def __init__(self):
        self.count = 0
        self.cache = {}

    def solve(self, num):
        if num in self.cache:
            self.count += self.cache[num]
            return

        if num == 0:
            self.cache[num] = 1
            self.count += 1
            return

        if num <= 2:
            self.cache[num] = num
            self.count += num
            return

        self.solve(num - 1)
        self.solve(num - 2)
        self.solve(num - 3)
        self.cache[num] = self.count


n = int(input())
stairs = Stairs()
stairs.solve(n)
print(stairs.count)

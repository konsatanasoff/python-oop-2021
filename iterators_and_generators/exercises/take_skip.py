class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        temp = self.current_value
        self.count -= 1
        self.current_value += self.step
        return temp


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)

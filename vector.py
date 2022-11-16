class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


thing = vector(1, 2)
print(thing.x * 2)
thing.x = thing.x * 5
print(thing.x)
thing.y += 5
print(thing.y)

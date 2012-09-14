from random import randint, choice

class Walk(object):
    def __init__(self, name):
        self.name = name
        self.steps = randint(1,10)
        self.movements = None

    def __str__(self):
        return "<Walk: %s (%s)>" % (self.name, self.steps)

    def __repr__(self):
        return "<Walk: %s (%s)>" % (self.name, self.steps)

    def move(self):
        if self.movements:
            print " ".join(self.movements)
        else:
            self._generate()
            self.move()

    def _generate(self):
        actions = ['shamble', 'stagger', 'roll', 'crawl', 'stumble']
        self.movements = [choice(actions) for x in range(self.steps)]

    def step(self):
        if self.movements:
            s = self.movements.pop(0)
            print s
        else:
            self._generate()
            self.step()

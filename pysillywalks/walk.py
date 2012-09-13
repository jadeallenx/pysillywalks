from random import randint, choice

class Walk(object):
    def __init__(self, name):
        self.name = name
        self.steps = randint(0,9)

    def __str__(self):
        return "<Walk: %s (%s)>" % (self.name, self.steps)

    def __repr__(self):
        return "<Walk: %s (%s)>" % (self.name, self.steps)

    def move(self):
        actions = ['shamble', 'stagger', 'roll', 'crawl', 'stumble']
        print " ".join([choice(actions) for x in range(self.steps)])


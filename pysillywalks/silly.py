from walk import Walk

class Silly(object):
    """
    Silly class

    Required keyword parameters:

        - ``walk`` - type of walk
        - ``silly`` - the level of silliness

    """

    def __init__(self, **kwargs):
        self.walk = Walk(kwargs['walk'])
        self.silly = kwargs['silly']
        self.is_very_silly = self.is_very_silly()

    def __str__(self):
        return "<Silly: %s>" % self.walk.name

    def __repr__(self):
        return "<Silly: %s>" % self.walk.name

    def action(self):
        self.walk.move()

    def is_very_silly(self):
        if self.silly > 3:
            return True
        else:
            return False

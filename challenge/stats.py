

class Stats:
    """
        This class is has basic functionalities to query built stats.
        Used in composition by DataCapture class.
    """

    def __init__(self, length, map):
        self.length = length
        self.map = map

    def less(self, value):
        return 0 if value == 0 else self.map[value-1]

    def greater(self, value):
        return self.length - self.map[value]

    def between(self, from_value, to_value):
        return self.map[to_value] - self.map[from_value-1]

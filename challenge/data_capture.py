from .stats import Stats


class DataCapture:
    """
        Creates an object to capture data & build stats.
    """

    def __init__(self):
        self.n_max = 1000
        self.items = []

    def add(self, value):
        self.items.append(value)

    def build_stats(self):
        length = len(self.items)
        # Create a cumulative counter to get stats easily
        index_map = [0] * self.n_max
        for i in self.items:
            if i < 0 or i >= self.n_max:
                print('Allowed values are positive integers less than %s'
                      % self.n_max)
                return
            index_map[i] += 1
        for i in range(self.n_max-1):
            index_map[i+1] += index_map[i]
        # Create stats object
        stats = Stats(length=length, map=index_map)
        return stats

import random
from bar import Bar

class DataGenerator:
    @staticmethod
    def GenerateDataSet(maximum=10000):
        Bar.bars.clear()
        return [Bar(random.randint(1, maximum + 1)) for _ in range(maximum+ 1)]
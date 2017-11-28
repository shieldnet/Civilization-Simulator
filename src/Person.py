class Person:

    def __init__(self, _food, _water, _tool, _population=0):
        self.food = _food
        self.water = _water
        self.tool = _tool
        self.population = _population

    # 자원소비

    def consume_food(self):

        self.food -= self.population * 0.5  # 임의로 정한 자원 소비식

    def consume_water(self):
        self.water -= self.population * 0.8  # 임의로 정한 자원 소비식

    # 인구수

    def get_pop(self):
        return self.population










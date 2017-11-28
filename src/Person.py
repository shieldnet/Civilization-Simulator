class Person:

    population = 0

    def __init__(self, _job):
        self.job = _job

        pass

    def consume(self, population):
        pass
        # 자원소비


class ToolMaker(Person):

    def make_tool(self):
        pass


class FoodMaker(Person):

    def make_food(self):
        pass


class WaterMaker(Person):

    def make_water(self):
        pass

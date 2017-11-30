class Person:
    # (food obj, water obj, tool obj, num_of_population)
    def __init__(self, _food, _water, _tool, _population=0):
        self._food = _food
        self._water = _water
        self._tool = _tool
        self._name = "Person"
        self._population = _population

    # 자원소비

    def consume_food(self):
        _food_consume_quantitiy = self._population * 0.5  # 임의로 정한 자원 소비식
        self._food.decrements(_food_consume_quantitiy)

    def consume_water(self):
        _water_consume_quantity = self._population * 0.8  # 임의로 정한 자원 소비식
        self._water.decrements(_water_consume_quantity)

    # 인구수

    def get_pop(self):
        return self._population

    def print_pop(self):
        print(" 인구수: ", self._population)

    def status_check(self):
        if self._water <= 0:
            print("{0} has no water to drink!\n", format(self._name))
        if self._food <= 0:
            print("{0} has no food to eat!\n", format(self._name))








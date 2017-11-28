class Person:

    def __init__(self, _food, _water, _tool, _population=0):
        self._food = _food
        self._water = _water
        self._tool = _tool
        self._population = _population

    # 자원소비

    def consume_food(self):

        self._food -= self._population * 0.5  # 임의로 정한 자원 소비식

    def consume_water(self):
        self._water -= self._population * 0.8  # 임의로 정한 자원 소비식

    # 인구수

    def get_pop(self):
        return self._population

    def person_status(self):
        print("총 인구수: ", self._population)










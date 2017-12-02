from Person import Person


class FoodMaker(Person):
    # ( number of has_tool, food object )
    def __init__(self, has_tool, _food, _water, _population=0):
        self._has_tool = has_tool
        self._food_obj = _food
        self._water_obj = _water
        self._population = _population
        self._name = "Food Maker"

    def make_food(self):
        _d_food = self._population * 1.2
        self._food_obj.increments(_d_food)

    def food_pop(self):
        print("Food Maker has tool : " + str(self._has_tool))
        print("Food Maker no tool : " + str(self._population - self._has_tool))


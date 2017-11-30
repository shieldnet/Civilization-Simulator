from Person import Person


class FoodMaker(Person):
    # ( number of has_tool, food object )
    def __init__(self, has_tool, _food):
        self._has_tool = has_tool
        self._food = _food
        self._name = "Food Maker"

    def make_food(self):
        _d_food = (self._has_tool * 0.8) + ((self._population - self._has_tool) * 0.5)
        self._food.increments(_d_food)

    def food_pop(self):
        print("Food Maker has tool : " + str(self._has_tool))
        print("Food Maker no tool : " + str(self._population - self._has_tool))


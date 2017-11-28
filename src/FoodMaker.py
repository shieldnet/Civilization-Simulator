from Person import Person


class FoodMaker(Person):
    def __init__(self, has_tool):
        self._has_tool = has_tool


    def make_food(self):
        self._tool += (self._has_tool * 0.8) + ((self._population - self._has_tool) * 0.5)

    def food_pop(self):
        print("Food Maker has tool : " + str(self._has_tool))
        print("Food Maker no tool : " + str(self._population - self._has_tool))


from Person import Person


class WaterMaker(Person):
    def __init__(self, has_tool, _food, _water, _population=0):
        self._has_tool = has_tool
        self._water_obj = _water
        self._food_obj = _food
        self._population = _population
        self._name = "Water Maker"

    def make_water(self):
        _water_increase = self._population * 2.2
        self._water_obj.increments(_water_increase)

    def water_pop(self):
        print("Water Maker has tool : " + str(self._has_tool))
        print("Water Maker no tool : " + str(self._population-self._has_tool))

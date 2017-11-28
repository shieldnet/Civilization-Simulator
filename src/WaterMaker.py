from Person import Person


class WaterMaker(Person):

    def __init__(self, has_tool):
        self._has_tool = has_tool

    def make_water(self):
        self._water += (self._has_tool * 0.8) + ((self._population-self._has_tool) * 0.5)

    def water_pop(self):
        print("Water Maker has tool : " + str(self._has_tool))
        print("Water Maker no tool : " + str(self._population-self._has_tool))
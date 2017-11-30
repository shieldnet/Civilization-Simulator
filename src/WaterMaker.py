from Person import Person


class WaterMaker(Person):
    def __init__(self, has_tool, _water_obj):
        self._has_tool = has_tool
        self._water_obj = _water_obj
        self._name = "Water Maker"

    def make_water(self):
        _water_increase = (self._has_tool * 0.8) + ((self._population - self._has_tool) * 0.5)
        self._water_obj.increments(_water_increase)

    def water_pop(self):
        print("Water Maker has tool : " + str(self._has_tool))
        print("Water Maker no tool : " + str(self._population-self._has_tool))

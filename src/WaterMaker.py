from Person import Person


class WaterMaker(Person):

    def __init__(self, has_tool):
        self.master_pop = has_tool
        self.normal_pop = self.population - self.master_pop

    def make_water(self):
        self.water += (self.master_pop * 0.8) + (self.normal_pop * 0.5)

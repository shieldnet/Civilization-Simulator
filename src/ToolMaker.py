from Person import Person


class ToolMaker(Person):

    def __init__(self, has_tool):
        self.master_pop = has_tool
        self.normal_pop = self.population - self.master_pop

    def make_tool(self):
        self.tool += (self.master_pop * 0.8) + (self.normal_pop * 0.5)
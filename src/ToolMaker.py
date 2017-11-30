from Person import Person


class ToolMaker(Person):
    def __init__(self, has_tool, _tool):
        self._has_tool = has_tool
        self._tool_obj = _tool
        self._name = "Tool Maker"
    """
    # We don't have tool yet.
    def make_tool(self):
        self._tool += (self._has_tool * 0.8) + ((self._population-self._has_tool) * 0.5)
    """
    
    def tool_pop(self):
        print("Tool Maker has tool : " + str(self._has_tool))
        print("Tool Maker no tool : " + str(self._population - self._has_tool))

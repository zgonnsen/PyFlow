from AbstractGraph import *


class AGIntNode(AGNode):
    def __init__(self, name):
        super(AGIntNode, self).__init__(name)
        self.name = name
        self.output = self.add_port('out', AGPortTypes.kOutput)
        self.set_data(0, False)

    def set_data(self, data, dirty_propagate=True):
        self.output.set_data(data, dirty_propagate)

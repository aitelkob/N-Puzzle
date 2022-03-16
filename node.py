class Node:
    def __init__(self,data,level=0,f=0):
        self.data = data
        self.level = level
        self.f = f
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

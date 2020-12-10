
'''
Parent class
'''''
class Node:
    def __init__(self):
        self.child = []

"""
Class for values
"""
class AtomNode(Node):
    def __init__(self, name, state):
        super().__init__()
        self.name = name
        self.state = state

    def __repr__(self):
        return self.name + " " + str(self.state)
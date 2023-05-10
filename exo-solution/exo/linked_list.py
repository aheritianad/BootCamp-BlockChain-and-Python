from bcbcpy import __author__


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, node: Node):
        # --- TO IMPLEMENT --
        ...
        # -------------------

    def add_to_tail(self, node: Node):
        # --- TO IMPLEMENT --
        ...
        # -------------------

    def remove_from_front(self):
        # --- TO IMPLEMENT --
        ...
        # -------------------

    def remove_from_tail(self):
        # --- TO IMPLEMENT --
        ...
        # -------------------

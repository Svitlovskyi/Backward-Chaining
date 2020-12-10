from Nodes import *

class RulesUtils:
    __operators = ["+", "=>", "|", "^", "!"]

    def check_is_all_node_is_known(self, child, node_store):
        for node in child:
            if node not in self.__operators:
                if node_store.get_node(node).state == None:
                    return False
        return True

    def transform_child_to_logical_operation(self, child, node_store):
        logical_operation = []
        for node_text in child:
            if node_text not in self.__operators:
                logical_operation.append(node_store.get_node(node_text).state)
                continue
            logical_operation.append(node_text)
        return logical_operation
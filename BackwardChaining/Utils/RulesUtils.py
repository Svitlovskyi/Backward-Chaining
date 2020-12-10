class RulesUtils:
    __operators = ["+", "=>", "|", "^", "!"]

    '''@input: child of node, current node store
       @return: bool and unknown node (or none, if all node is known)
    '''
    def check_is_all_node_is_known(self, child, node_store):
        unknown_node = None
        for node in child:
            if node not in self.__operators:
                if node_store.get_node(node).state == None:
                    return False, node_store.get_node(node)
        return True, unknown_node

    '''@input: child, node store
       @return: transformed node name in logical operation to values
    '''
    def transform_child_to_logical_operation(self, child, node_store):
        logical_operation = []
        for node_text in child:
            if node_text not in self.__operators:
                logical_operation.append(node_store.get_node(node_text).state)
                continue
            logical_operation.append(node_text)
        return logical_operation
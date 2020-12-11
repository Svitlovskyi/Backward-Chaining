class RulesUtils:
    __operators = ["+", "=>", "|", "^", "!", "(", ")"]

    '''@input: child of node, current node store
       @return: bool and unknown node (or none, if all node is known)
    '''
    def check_is_all_node_is_known(self, child, node_store):
        unknown_nodes = []
        for node in child:
            if node not in self.__operators:
                init_node_from_child = node_store.get_node(node)
                if init_node_from_child.state == None:
                    unknown_nodes.append(init_node_from_child)
        if len(unknown_nodes) > 0:
            return False, unknown_nodes
        return True, None

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
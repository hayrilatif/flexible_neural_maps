class SingularNode:
    def __init__(self):
        self.name=None
        self.node_value=0
        self.resources_list=[]

    def get_resource_count(self):
        return len(self.resources_list)

    def reverse_information_flow(self):
        for resource in self.resources_list:
            resource.resource_node.reverse_information_flow()
            self.node_value+=resource.resource_node.node_value*resource.weight
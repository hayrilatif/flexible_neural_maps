from fsnm.nodes.input_node import InputNode
from fsnm.nodes.hidden_node import Node
from fsnm.nodes.output_node import OutputNode
from fsnm.nodes.connection import Connection

class Plasma:
    def __init__(self):
        self.input_node_list={}
        self.hidden_node_list={}
        self.output_node_list={}
    
    def get_universal_node_dictionary(self):
        merge=self.input_node_list.copy()
        merge.update(self.hidden_node_list)
        merge.update(self.output_node_list)

        return merge

    def add_input_node(self,name):
        node=InputNode()
        node.name=name
        self.input_node_list[name]=node

    def add_hidden_node(self,name):
        node=Node()
        node.name=name
        self.hidden_node_list[name]=node

    def add_output_node(self,name):
        node=OutputNode()
        node.name=name
        self.output_node_list[name]=node

    def connect(self,weight,name_resource,name_post):
        nodes=self.get_universal_node_dictionary()
        connection=Connection(weight,resource_node=nodes[name_resource])
        nodes[name_post].resources_list.append(connection)




    
from fsnm.nodes.input_node import InputNode
from fsnm.nodes.hidden_node import Node
from fsnm.nodes.output_node import OutputNode
from fsnm.nodes.singular_node import SingularNode
from fsnm.nodes.connection import Connection
from fsnm import *

in1=InputNode()
in1.node_value=10

cn1=Connection(0.1,in1)

hn1=Node()
hn1.resources_list.append(cn1)

cn2=Connection(0.1,hn1)

on1=OutputNode()
on1.resources_list.append(cn2)

singular_conn=Connection(1,on1)

singular=SingularNode()
singular.resources_list.append(singular_conn)

singular.reverse_information_flow()


print(on1.node_value)
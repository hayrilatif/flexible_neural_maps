from fsnm.nodes.input_node import InputNode
from fsnm.nodes.hidden_node import Node
from fsnm.nodes.output_node import OutputNode
from fsnm.nodes.singular_node import SingularNode
from fsnm.nodes.connection import Connection
from fsnm import *
from fsnm.plasma import Plasma

plasma=Plasma()

plasma.add_input_node("in1")
plasma.add_hidden_node("hn1")
plasma.add_output_node("on1")

plasma.connect(0.1,"in1","hn1")
plasma.connect(0.1,"hn1","on1")

plasma.input_node_list["in1"].node_value=10

plasma.output_node_list["on1"].reverse_information_flow()



print(plasma.output_node_list["on1"].node_value)
class InputNode:
    def __init__(self):
        self.name=None
        self.node_value=0

    def reverse_information_flow(self):
        print(self.node_value)
        print("end of tree <EOT>")
        pass
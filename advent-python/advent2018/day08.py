class Node:
    def __init__(self: Node):
        self.children: list[Node] = []
        self.metadata: list[int] = []

    def deep_metadata_sum(self: Node) -> int:
        return sum(self.metadata) + sum([child.deep_metadata_sum() for child in self.children])
    
    def value(self: Node) -> int:
        if len(self.children) == 0:
            return sum(self.metadata)
        else:
            total_value: int = 0
            for i in self.metadata:
                if 0 < i <= len(self.children):
                    total_value += self.children[i-1].value()
            return total_value
    

def parse_node(numbers: list[int]) -> Node:
    new_node: Node = Node()
    num_children: int = numbers.pop(0)
    num_metadata: int = numbers.pop(0)
    for _ in range(num_children):
        new_node.children.append(parse_node(numbers))
    for _ in range(num_metadata):
        new_node.metadata.append(numbers.pop(0))
    return new_node


with open("input-08.txt") as f:
    data:str = f.read().strip()

#Part 1
numbers: list[int] = [int(x) for x in data.split()]
nodes: list[Node] = []
while len(numbers) > 0:
    nodes.append(parse_node(numbers))

print(sum([node.deep_metadata_sum() for node in nodes]))


#Part 2
numbers: list[int] = [int(x) for x in data.split()]
nodes: list[Node] = []
while len(numbers) > 0:
    nodes.append(parse_node(numbers))

print(nodes[0].value())
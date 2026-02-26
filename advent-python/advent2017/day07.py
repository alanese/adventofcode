from collections import Counter, defaultdict

def common_diff_values(values: list[int]) -> tuple[int, int]:
    """
    Docstring for common_diff_values
    
    :param values: A list of at least three integers, all identical except one
    :type values: list[int]
    :return: a tuple consisting of the common value and the different value
    :rtype: tuple[int, int]
    """
    common: int = -1
    different: int = -1
    for val, count in Counter(values).items():
        if count > 1:
            common = val
        else:
            different = val
    return common, different

class TreeNode:
    nodes: dict[str, TreeNode] = defaultdict(lambda: TreeNode())

    def __init__(self: TreeNode):
        self.parent: str = ""
        self.weight: int = 0
        self.children: list[str] = []

    def total_weight(self: TreeNode) -> int:
        weight: int = self.weight
        for child in self.children:
            weight += TreeNode.nodes[child].total_weight()
        return weight
    
    def is_balanced(self: TreeNode) -> bool:
        if len(self.children) < 1:
            return True
        
        first_weight: int = TreeNode.nodes[self.children[0]].total_weight()
        for child in self.children[1:]:
            if TreeNode.nodes[child].total_weight() != first_weight:
                return False
        return True

#nodes: dict[str, TreeNode] = defaultdict(lambda: TreeNode())

some_id: str = ""
with open("input-07.txt") as f:
    for line in f:
        line_split: list[str] = line.strip().split(maxsplit=3)
        id: str = line_split[0]
        some_id = id
        weight: int = int(line_split[1][1:-1])
        TreeNode.nodes[id].weight = weight
        if len(line_split) > 2:
            TreeNode.nodes[id].children = line_split[3].split(", ")
            for child_id in TreeNode.nodes[id].children:
                TreeNode.nodes[child_id].parent = id

while TreeNode.nodes[some_id].parent != "":
    some_id = TreeNode.nodes[some_id].parent

print(some_id)

unbalanced_id: str = some_id

weights: list[int] = []

#Find the ID of the unbalanced node
while not TreeNode.nodes[unbalanced_id].is_balanced():
    weights = [TreeNode.nodes[child_id].total_weight() for child_id in TreeNode.nodes[unbalanced_id].children]
    _, diff = common_diff_values(weights)
    unbalanced_id = TreeNode.nodes[unbalanced_id].children[weights.index(diff)]

#Find its total weight and the total weight of its siblings, compute the difference, add to its weight to find target weight
common, diff = common_diff_values(weights)
unbalanced_id = TreeNode.nodes[unbalanced_id].parent
unbalanced_node: TreeNode = TreeNode.nodes[unbalanced_id]
offset = common - diff

off_weight_child_index: int = weights.index(diff)
off_weight_child_id: str = unbalanced_node.children[off_weight_child_index]
off_weight_child: TreeNode = TreeNode.nodes[off_weight_child_id]
print(f"Node {off_weight_child_id} should have weight {off_weight_child.weight + offset}")
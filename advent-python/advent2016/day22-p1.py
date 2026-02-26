from typing import NamedTuple

class StorageNode(NamedTuple):
    x: int
    y: int
    size: int
    used: int
    available: int
    use_percentage: int

def parse_coords(node_id: str) -> tuple[int, int]:
    node_id_split: list[str] = node_id[16:].split("-y")
    return int(node_id_split[0]), int(node_id_split[1])

def parse_df_line(line: str) -> StorageNode:
    line_split: list[str] = line.split()
    x: int
    y: int
    x, y = parse_coords(line_split[0])
    size: int = int(line_split[1][:-1])
    used: int = int(line_split[2][:-1])
    available: int = int(line_split[3][:-1])
    use_percentage: int = int(line_split[4][:-1])
    return StorageNode(x=x, y=y, size=size, used=used, available=available, use_percentage=use_percentage)

def viable_pair(node_A: StorageNode, node_B: StorageNode) -> bool:
    return node_A.used != 0 and node_A.used <= node_B.available

with open("input-22.txt") as f:
    lines: list[str] = f.readlines()

nodes: dict[tuple[int, int], StorageNode] = {}
for line in lines[2:]:
    node: StorageNode = parse_df_line(line.strip())
    nodes[(node.x, node.y)] = node


x: int
y: int
viable_count: int = 0
nodes_list: list[tuple[tuple[int, int], StorageNode]] = list(nodes.items())
for i, ((x1,y1), node1) in enumerate(nodes_list):
    for (x2, y2), node2 in nodes_list[i+1:]:
        if viable_pair(node1, node2):
            viable_count += 1
        if viable_pair(node2, node1):
            viable_count += 1
print(viable_count)


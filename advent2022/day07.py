class Directory:
    def __init__(self: Directory, id: str, parent: Directory | None):
        self.id = id
        self.parent: Directory | None = parent
        self.file_sizes: list[int] = []
        self.children: dict[str, Directory] = {}

    def total_size(self: Directory) -> int:
        return sum(self.file_sizes) + sum(child.total_size() for child in self.children.values())
    
with open("input-07.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Build directory tree
root_node: Directory = Directory("/", None)
cur_node: Directory = root_node
path: list[str] = []
for line in data:
    if line.startswith("$ cd"):
        next_dir: str = line.split()[-1]
        if next_dir == "/":
            cur_node = root_node
        elif next_dir == "..":
            if cur_node.parent is None:
                raise Exception("Current node is root")
            cur_node = cur_node.parent
        else:
            cur_node = cur_node.children[next_dir]
    elif line.startswith("$ ls"):
        continue
    else:
        fst, _, snd = line.partition(" ")
        if fst == "dir":
            subfolder: Directory = Directory(snd, cur_node)
            cur_node.children[snd] = subfolder
        else:
            cur_node.file_sizes.append(int(fst))

#Parts 1, 2
size_threshold: int = 100_000
DISK_SIZE: int = 70_000_000
free_space: int = DISK_SIZE - root_node.total_size()
to_free: int = 30_000_000 - free_space
smallest_id: str = "ERROR"
smallest_size: int = DISK_SIZE
size_sum: int = 0
queue: list[Directory] = [root_node]

while len(queue) > 0:
    next: Directory = queue.pop(0)
    size: int = next.total_size()
    if size <= size_threshold:
        size_sum += size
    if size >= to_free and size < smallest_size:
        smallest_id = next.id
        smallest_size = size
    for subfolder in next.children.values():
        queue.append(subfolder)
print(size_sum)
print(smallest_size)

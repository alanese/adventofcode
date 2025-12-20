class CircleNode:
    def __init__(self: CircleNode, value: int):
        self.value: int = value
        self.next: CircleNode = self
        self.prev: CircleNode = self

    def insert_after(self: CircleNode, value: int):
        new_node: CircleNode = CircleNode(value)
        new_node.prev = self
        new_node.next = self.next
        new_node.prev.next = new_node
        new_node.next.prev = new_node

    def remove_after(self: CircleNode) -> int:
        if self.next == self:
            raise Exception("No next node to remove")
        
        value = self.next.value
        self.next.next.prev = self
        self.next = self.next.next
        return value
    
PLAYER_COUNT: int = 413
LAST_MARBLE: int = 71082

#Part 1
current_player: int = 0
scores: list[int] = [0] * PLAYER_COUNT

current_marble = CircleNode(0)

for marble in range(1, LAST_MARBLE+1):
    if marble % 23 == 0:
        scores[current_player] += marble
        for _ in range(8):
            current_marble = current_marble.prev
        scores[current_player] += current_marble.remove_after()
        current_marble = current_marble.next
    else:
        current_marble.next.insert_after(marble)
        current_marble = current_marble.next.next
    current_player = (current_player + 1) % PLAYER_COUNT

print(max(scores))

#Part 2
current_player = 0
scores = [0] * PLAYER_COUNT

current_marble = CircleNode(0)

for marble in range(1, LAST_MARBLE*100+1):
    if marble % 23 == 0:
        scores[current_player] += marble
        for _ in range(8):
            current_marble = current_marble.prev
        scores[current_player] += current_marble.remove_after()
        current_marble = current_marble.next
    else:
        current_marble.next.insert_after(marble)
        current_marble = current_marble.next.next
    current_player = (current_player + 1) % PLAYER_COUNT

print(max(scores))
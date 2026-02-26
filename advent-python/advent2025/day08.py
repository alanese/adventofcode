class UnionSet:
    def __init__(self, *children):
        self.parent = None
        self.children = children
        for child in self.children:
            child.parent = self
    
    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root()
    
    def size(self):
        if self.children is None or len(self.children) == 0:
            return 1
        else:
            return sum([child.size() for child in self.children])
        

def distance(t1, t2):
    sqr_sum = sum([(x-y)**2 for x,y in zip(t1, t2)])
    return sqr_sum**(1/2)

def product(vals):
    if len(vals) == 0:
        return 1
    else:
        p = 1
        for v in vals:
            p *= v
        return p
    

with open("input-08.txt") as f:
    triples = [ tuple(int(x) for x in line.strip().split(",")) for line in f]

pairs = []
for i, t1 in enumerate(triples):
    for t2 in triples[i+1:]:
        pairs.append((distance(t1, t2), t1, t2))

pairs.sort()

circuits = {triple: UnionSet() for triple in triples}

for _, t1, t2 in pairs[:1000]:
    if circuits[t1].root() != circuits[t2].root():
        UnionSet(circuits[t1].root(), circuits[t2].root())


sizes = [v.size() for v in set(c.root() for c in circuits.values())]
sizes.sort(reverse=True)
print(product(sizes[:3]))

#--------

circuits = {triple: UnionSet() for triple in triples}

for _, t1, t2 in pairs:
    if circuits[t1].root() != circuits[t2].root():
        UnionSet(circuits[t1].root(), circuits[t2].root())
        if circuits[t1].root().size() == len(triples):
            print(t1[0] * t2[0])
            break

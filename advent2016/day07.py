#Common def
def classify_subsequences(sequence: str) -> tuple[list[str], list[str]]:
    supernet: list[str] = []
    hypernet: list[str] = []
    current_subseq: str = ""
    in_brackets: bool = False
    for chr in sequence:
        if in_brackets:
            if chr == "]":
                in_brackets = False
                if current_subseq != "":
                    hypernet.append(current_subseq)
                    current_subseq = ""
            else:
                current_subseq += chr
        elif chr == "[":
            in_brackets = True
            if current_subseq != "":
                supernet.append(current_subseq)
                current_subseq = ""
        else:
            current_subseq += chr
    if current_subseq != "":
        supernet.append(current_subseq)

    return supernet, hypernet

#Defs for part 1

def contains_abba(test: str) -> bool:
    for i in range(len(test)-3):
        if test[i] == test[i+3] and test[i+1] == test[i+2] and test[i] != test[i+1]:
            return True
    return False

def supports_tls(ip: str) -> bool:
    supernet, hypernet = classify_subsequences(ip)
    for subseq in hypernet:
        if contains_abba(subseq):
            return False
    for subseq in supernet:
        if contains_abba(subseq):
            return True
    return False

# Defs for part 2

def get_aba_patterns(sequence: str) -> list[str]:
    seqs: list[str] = []
    for i in range(len(sequence)-2):
        if sequence[i] == sequence[i+2] and sequence[i] != sequence[i+1]:
            seqs.append(sequence[i:i+3])
    return seqs

def get_abas_babs(ip: str) -> tuple[set[str], set[str]]:
    abas: set[str] = set()
    babs: set[str] = set()
    supernets: list[str]
    hypernets: list[str]
    supernets, hypernets = classify_subsequences(ip)
    for supernet in supernets:
        for aba in get_aba_patterns(supernet):
            abas.add(aba)
    for hypernet in hypernets:
        for bab in get_aba_patterns(hypernet):
            babs.add(bab)
    return abas, babs

def flip_aba(aba: str) -> str:
    if len(aba) != 3 or aba[0] == aba[1] or aba[0] != aba[2]:
        raise ValueError(f"Invalid pattern: {aba}")
    return aba[1] + aba[0] + aba[1]

def supports_ssl(ip: str) -> bool:
    abas: set[str]
    babs: set[str]
    abas, babs = get_abas_babs(ip)
    for aba in abas:
        if flip_aba(aba) in babs:
            return True
    return False

#Output:
tls_count: int = 0
ssl_count: int = 0
with open("input-07.txt") as f:
    for line in f:
        line = line.strip()
        if supports_tls(line):
            tls_count += 1
        if supports_ssl(line):
            ssl_count += 1
print(tls_count)
print(ssl_count)
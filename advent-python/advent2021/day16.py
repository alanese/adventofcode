from math import prod

class Packet:
    version: int
    type_id: int
    payload: int | list[Packet]

    def __init__(self: Packet, ver: int, type_id: int, payload: int | list[Packet]):
        self.version = ver
        self.type_id = type_id
        self.payload = payload

    def version_sum(self: Packet) -> int:
        if isinstance(self.payload, int):
            return self.version
        else:
            return self.version + sum(subpacket.version_sum() for subpacket in self.payload)
        
    def evaluate(self: Packet) -> int:
        if isinstance(self.payload, int):
            return self.payload
        else:
            match self.type_id:
                case 0:
                    return sum(packet.evaluate() for packet in self.payload)
                case 1:
                    return prod(packet.evaluate() for packet in self.payload)
                case 2:
                    return min(packet.evaluate() for packet in self.payload)
                case 3:
                    return max(packet.evaluate() for packet in self.payload)
                case 5:
                    return 1 if self.payload[0].evaluate() > self.payload[1].evaluate() else 0
                case 6:
                    return 1 if self.payload[0].evaluate() < self.payload[1].evaluate() else 0
                case 7:
                    return 1 if self.payload[0].evaluate() == self.payload[1].evaluate() else 0
                case _:
                    raise ValueError(f"Invalid type id {self.type_id}")


#Returns value as an int and unprocessed bits as a str
def parse_literal(bits: str) -> tuple[int, str]:
    bin_val: str = ""
    chunk: str = "1"
    while chunk[0] == "1":
        chunk = bits[:5]
        bits = bits[5:]
        bin_val += chunk[1:]
    return int(bin_val, base=2), bits

#Returns packet and remaining unprocessed data
def parse_packet(bits: str) -> tuple[Packet, str]:
    version: int = int(bits[:3], base=2)
    type_id: int = int(bits[3:6], base=2)
    bits = bits[6:]
    if type_id == 4:
        payload, bits = parse_literal(bits)
        return Packet(version, type_id, payload), bits
    else:
        length_id: str = bits[0]
        if length_id == "1":
            subpacket_count: int = int(bits[1:12], base=2)
            bits = bits[12:]
            payload_packets: list[Packet] = []
            for _ in range(subpacket_count):
                packet, bits = parse_packet(bits)
                payload_packets.append(packet)
            return Packet(version, type_id, payload_packets), bits
        else:
            payload_length: int = int(bits[1:16], base=2)
            bits = bits[16:]
            init_length: int = len(bits)
            payload_packets: list[Packet] = []
            while init_length - len(bits) < payload_length:
                packet, bits = parse_packet(bits)
                payload_packets.append(packet)
            return Packet(version, type_id, payload_packets), bits

with open("input-16.txt") as f:
    data: str = f.read().strip()
binary: str = f"{int(data, base=16):b}"

#Part 1
packet, _ = parse_packet(binary)
print(packet.version_sum())

#Part 2
print(packet.evaluate())

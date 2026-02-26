def low_bits(x: int, num_bits: int) -> int:
    return x & ((1<<num_bits) - 1)


A_FACTOR: int = 16807
B_FACTOR: int = 48271
MODULUS: int = 2147483647
A_INIT: int = 679
B_INIT: int = 771
generator_a: int = A_INIT
generator_b: int = B_INIT
matches: int = 0
for iteration in range(40000000):
    if iteration % 10000 == 0:
        print(iteration)
    generator_a = (generator_a * A_FACTOR) % MODULUS
    generator_b = (generator_b * B_FACTOR) % MODULUS
    if low_bits(generator_a, 16) == low_bits(generator_b, 16):
        matches += 1

print(matches)

#------------

generator_a = A_INIT
generator_b = B_INIT
matches = 0
for iteration in range(5000000):
    if iteration % 10000 == 0:
        print(iteration)
    generator_a = (generator_a * A_FACTOR) % MODULUS
    while generator_a % 4 != 0:
        generator_a = (generator_a * A_FACTOR) % MODULUS
    generator_b = (generator_b * B_FACTOR) % MODULUS
    while generator_b % 8 != 0:
        generator_b = (generator_b * B_FACTOR) % MODULUS
    if low_bits(generator_a, 16) == low_bits(generator_b, 16):
        matches += 1

print(matches)
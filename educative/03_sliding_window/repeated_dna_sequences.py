def find_repeated_sequences(dna: str, k: int) -> set[str]:
    n = len(dna)
    visited_seq = set()
    repeated_seq = set()
    start = 0

    for end in range(k, n + 1):
        seq = dna[start:end]
        seq_hash = dna_hash(seq)
        # print(f"seq = {seq}, hash = {seq_hash}")
        if seq_hash in visited_seq:
            repeated_seq.add(seq)
        visited_seq.add(seq_hash)
        start += 1

    return repeated_seq


def dna_hash(seq) -> int:
    table = {"A": 0, "T": 1, "C": 2, "G": 3}
    seq_hash = 0
    p = 31
    m = 10**9 + 9
    for i, char in enumerate(seq):
        seq_hash += (table[char] * (p**i)) % m
    return seq_hash


if __name__ == "__main__":
    inputs = [("AGCTGAAAGCTTAGCTG", 5)]

    for dna, k in inputs:
        repeated_seq = find_repeated_sequences(dna, k)
        print(f"dna = {dna}, k = {k}, repeated_seq = {repeated_seq}")

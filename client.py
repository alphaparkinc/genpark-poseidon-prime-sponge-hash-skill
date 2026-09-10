class PoseidonSponge:
    """
    Poseidon Prime Field Sponge Hash Function.
    Algebraic hash optimized for zero-knowledge arithmetic circuits (R1CS, AIR).
    """
    def __init__(self, p=10007):
        self.p = p

    def sbox(self, x):
        # Quintic power S-box: x^5 mod p
        return pow(x, 5, self.p)

    def hash_pair(self, left, right):
        # 2-word internal state
        s0 = (left + 1) % self.p
        s1 = (right + 2) % self.p

        # Multi-round substitution and MDS linear mixing
        for _ in range(3):
            s0 = self.sbox(s0)
            s1 = self.sbox(s1)
            # MDS matrix multiplication [[2, 3], [1, 2]]
            new_s0 = (2 * s0 + 3 * s1) % self.p
            new_s1 = (s0 + 2 * s1) % self.p
            s0, s1 = new_s0, new_s1

        return s0

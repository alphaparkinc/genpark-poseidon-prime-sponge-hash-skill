from client import PoseidonSponge

def main():
    print("=== Testing Poseidon Prime Field Sponge Hash ===")
    pos = PoseidonSponge()
    
    h1 = pos.hash_pair(10, 20)
    h2 = pos.hash_pair(10, 20)
    h3 = pos.hash_pair(10, 21)
    
    print(f"Hash(10, 20) = {h1}")
    print(f"Hash(10, 20) = {h2} (Determinism check)")
    print(f"Hash(10, 21) = {h3} (Collision resistance check)")
    
    assert h1 == h2, "Poseidon must be deterministic"
    assert h1 != h3, "Poseidon must produce distinct hashes for distinct inputs"
    print("=== Poseidon Hash Verification Complete ===")

if __name__ == "__main__":
    main()

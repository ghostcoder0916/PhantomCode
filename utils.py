import hashlib

def generate_hash(message):
    """
    Generate a SHA256 hash of the input message.
    Useful for cryptographic verification.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode('utf-8'))
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    message = "PhantomMessage"
    print(f"SHA256 Hash: {generate_hash(message)}")

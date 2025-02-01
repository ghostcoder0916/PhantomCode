import base64

def decrypt_message(encoded_message):
    """
    Decrypt the given message by reversing base64 encoding.
    The message should be encoded in base64.
    """
    decoded_bytes = base64.b64decode(encoded_message)
    return decoded_bytes.decode('utf-8')

if __name__ == "__main__":
    # Hidden flag encoded in base64
    encoded_message = "U1RBUl9WRUVYZg=="
    decrypted_message = decrypt_message(encoded_message)
    
    # Print the decrypted message (flag)
    print(f"Decrypted message: {decrypted_message}")

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.fernet import Fernet
import os

class AstraCrypt:
    """
    A unified encryption bridge for secure P2P communication.
    Supports RSA for identity/key-exchange and Fernet (AES) for high-speed data.
    """
    def __init__(self):
        # Local Node Identity
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

    def get_public_key_pem(self) -> str:
        """Export public key for sharing with peers."""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

    def encrypt_for_peer(self, data: bytes, peer_pub_key_pem: str) -> bytes:
        """Encrypt sensitive data using a peer's public RSA key."""
        peer_key = serialization.load_pem_public_key(peer_pub_key_pem.encode())
        return peer_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt_mine(self, encrypted_data: bytes) -> bytes:
        """Decrypt data meant for this node using its private RSA key."""
        return self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def create_session_handler(key: str = None):
        """Creates a symmetric Fernet handler for bulk data transfer."""
        if not key:
            key = Fernet.generate_key()
        return Fernet(key), key

# Example usage pattern:
# 1. Exchange RSA Public Keys.
# 2. Node A creates a session key: cipher, key = AstraCrypt.create_session_handler()
# 3. Node A encrypts the key for Node B: encrypted_key = node_a.encrypt_for_peer(key, node_b_pub_pem)
# 4. Node B decrypts the session key: session_key = node_b.decrypt_mine(encrypted_key)

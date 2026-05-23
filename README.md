# ðŸ›¡ï¸ Astra Crypt

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Security: High](https://img.shields.io/badge/security-industrial--grade-red.svg)](#)

**Astra Crypt** is a lightweight, high-performance encryption bridge designed for P2P networks and distributed systems. It seamlessly combines **RSA (Asymmetric)** for identity and key exchange with **Fernet (Symmetric AES)** for high-speed data encryption.

## ðŸš€ Features
- **Node Identity:** Automatic generation of 2048-bit RSA key pairs.
- **Secure Handshakes:** Easy public key serialization for peer-to-peer exchange.
- **Hybrid Encryption:** Use RSA to securely share AES session keys.
- **Developer Friendly:** Clean, object-oriented API for complex cryptographic flows.

## ðŸ› ï¸ Installation
```bash
pip install cryptography
```

## ðŸ’» Quick Start
```python
from astra_crypt import AstraCrypt

# Initialize your node
node = AstraCrypt()
pub_key = node.get_public_key_pem()

# Encrypt data for a peer (using their public key)
encrypted = node.encrypt_for_peer(b"Sensitive Data", peer_pub_key)

# Decrypt data sent to you
decrypted = node.decrypt_mine(encrypted)
```

## ðŸ¤ Contributing
Help us make distributed systems more secure. Issues and pull requests are welcome.

---
Built with âš¡ by [David Selorm Walker](https://github.com/selormwalker)

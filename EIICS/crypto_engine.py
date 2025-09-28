"""
crypto_engine.py
AES-256 CBC Encryption Engine for EIICS
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import HMAC, SHA256
import base64

class CryptoEngine:
    """Professional AES-256 CBC Encryption Engine with HMAC authentication"""
    
    # Constants
    SALT_SIZE = 16
    IV_SIZE = AES.block_size
    HMAC_KEY_SIZE = 32
    ITERATION_COUNT = 1000000
    
    @staticmethod
    def _derive_keys(key: str, salt: bytes) -> tuple:
        """Derive encryption and HMAC keys using PBKDF2"""
        # Derive 64 bytes: 32 for encryption, 32 for HMAC
        derived_key = PBKDF2(key, salt, 64, count=CryptoEngine.ITERATION_COUNT)
        enc_key = derived_key[:32]
        hmac_key = derived_key[32:]
        return enc_key, hmac_key

    @staticmethod
    def encrypt_data(plaintext: bytes, key: str) -> str:
        """Encrypt data using AES-256 CBC with HMAC authentication"""
        # Generate random salt and IV
        salt = get_random_bytes(CryptoEngine.SALT_SIZE)
        iv = get_random_bytes(CryptoEngine.IV_SIZE)
        
        # Derive keys
        enc_key, hmac_key = CryptoEngine._derive_keys(key, salt)
        
        # Encrypt the data
        cipher = AES.new(enc_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        
        # Create HMAC of (iv + ciphertext)
        hmac_data = iv + ciphertext
        hmac = HMAC.new(hmac_key, hmac_data, digestmod=SHA256)
        hmac_digest = hmac.digest()
        
        # Combine all components
        encrypted_data = salt + iv + ciphertext + hmac_digest
        return base64.b64encode(encrypted_data).decode('utf-8')

    @staticmethod
    def decrypt_data(encrypted_data_b64: str, key: str) -> bytes:
        """Decrypt data using AES-256 CBC with HMAC verification"""
        try:
            encrypted_data = base64.b64decode(encrypted_data_b64)
            
            # Extract components
            salt = encrypted_data[:CryptoEngine.SALT_SIZE]
            iv = encrypted_data[CryptoEngine.SALT_SIZE:CryptoEngine.SALT_SIZE + CryptoEngine.IV_SIZE]
            ciphertext = encrypted_data[CryptoEngine.SALT_SIZE + CryptoEngine.IV_SIZE:-32]
            received_hmac = encrypted_data[-32:]
            
            # Derive keys
            enc_key, hmac_key = CryptoEngine._derive_keys(key, salt)
            
            # Verify HMAC
            hmac_data = iv + ciphertext
            hmac = HMAC.new(hmac_key, hmac_data, digestmod=SHA256)
            hmac.verify(received_hmac)
            
            # Decrypt the data
            cipher = AES.new(enc_key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            return plaintext
            
        except (ValueError, KeyError) as e:
            raise ValueError("Decryption failed. Invalid key or corrupted data.") from e
        except Exception as e:
            raise ValueError("Authentication failed. Data may have been tampered with.") from e

if __name__ == "__main__":
    # Test the crypto engine
    test_key = "my_very_secure_secret_key_123!"
    test_data = "Hello, this is a test message for the enhanced crypto engine!"
    
    encrypted = CryptoEngine.encrypt_data(test_data.encode(), test_key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = CryptoEngine.decrypt_data(encrypted, test_key)
    print(f"Decrypted: {decrypted.decode()}")
    
    # Test with wrong key
    try:
        CryptoEngine.decrypt_data(encrypted, "wrong_key")
    except ValueError as e:
        print(f"Expected error with wrong key: {e}")
import json
import gzip
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet

from core.config import config

def decrypt_and_decompress_instance_payload(encrypted_symmetric_key: str, cipher_text: str) -> dict:
     """
     Decrypts and decompresses data encrypted and compressed using AES symmetric encryption and RSA asymmetric encryption.

     Args:
          encrypted_symmetric_key (str): The base64-encoded encrypted symmetric key.
          cipher_text (str): The base64-encoded encrypted data.

     Returns:
          dict: The decrypted and decompressed JSON-formatted data.
     """
     # Decode base64 strings
     encrypted_symmetric_key = base64.b64decode(encrypted_symmetric_key)
     cipher_text = base64.b64decode(cipher_text)

     # Convert base64 strings back to key objects
     private_key = serialization.load_pem_private_key(
          base64.b64decode(config.INSTANCE_PAYLOAD_PRIVATE_KEY),
          password=None,
          backend=default_backend()
     )

     # Decrypt symmetric key with private key
     symmetric_key = private_key.decrypt(
          encrypted_symmetric_key,
          padding.OAEP(
               mgf=padding.MGF1(algorithm=hashes.SHA256()),
               algorithm=hashes.SHA256(),
               label=None
          )
     )
     
     # Decrypt compressed data with symmetric key (AES)
     fernet = Fernet(symmetric_key)
     decrypted_data = fernet.decrypt(cipher_text)
     
     # Decompress data
     json_data = gzip.decompress(decrypted_data)
     
     # Convert JSON data to Python object
     data = json.loads(json_data.decode('utf-8'))
     
     return data

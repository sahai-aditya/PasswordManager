from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self):
        """
        Class to save encrypted passwords, delete, update and fetch decrypted passwords.
        """

"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import bcrypt


class Hash:
    """
     Hash Plain Values using Python bcrypt (https://pypi.org/project/bcrypt/)
    Example Usage
    hashed_password = Hash.encrypt(text_to_encrypt)

    To make use of the new Key Defined Function (KDF), use
    hashed_password = Hash.encrypt(text_to_encrypt, method='kdf')

    To check if hashed password is the same as a plain text

    is_same = Hash.compare(plain_text, hashed_text)

    """
    @classmethod
    def encrypt(cls, plain_text, method='normal'):
        plain_text = str(plain_text).encode('utf-8')
        if method is 'kdf':
            return bcrypt.kdf(password=plain_text, salt=cls.gensalt(12), desired_key_bytes=32, rounds=100)
        return bcrypt.hashpw(plain_text, cls.gensalt(12))

    @classmethod
    def compare(cls, plain_text, hash_text):
        plain_text = str(plain_text).encode('utf-8')
        return bcrypt.checkpw(plain_text, hash_text)

    @classmethod
    def gensalt(cls, rounds=12, prefix=b"2b"):
        return bcrypt.gensalt(rounds, prefix)


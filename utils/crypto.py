# coding=utf-8
from passlib.context import Cryptcontext

class Crypto:

    def __init__(self):
        self.pwd_context = Cryptcontext(schemes=["bcrypt"], deprecated="auto")

    def encrypt(self, secret):
        return self.pwd_context.hash(secret)

    def verify(self, secret, hash):
        return self.pwd_context.verify(secret, hash)

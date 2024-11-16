from random import random, choices

class Bitcoin:

    to_eur = 1

    @staticmethod
    def update(iterations = 1):

        percentage = random() / 100

        # negate
        if choices([1, 0])[0]:
            percentage *= -1

        # apply
        Bitcoin.to_eur += (Bitcoin.to_eur * percentage)
        return percentage
        
class Wallet:

    eur = 0
    btc = 0

    def deposit(self, eur):
        self.eur += eur

    def withdraw(self, eur):
        self.eur -= eur

    def buy(self, eur):

        self.eur -= eur
        self.btc += eur / Bitcoin.to_eur
    
    def sell(self, btc):
        
        self.btc -= btc
        self.eur += btc * Bitcoin.to_eur
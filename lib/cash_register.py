#!/usr/bin/env python3
class CashRegister:
    def __init__(self):
        self.items = []
        self.total = 0
        self.last_transaction = 0

    def add_item(self, item, quantity, price):
        self.items.append((item, quantity, price))
        self.total += quantity * price

    def apply_discount(self, discount_percentage):
        discount_amount = self.total * (discount_percentage / 100)
        return self.total - discount_amount

    def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.last_transaction = 0

    def get_items(self):
        return self.items

    def get_total(self):
        return self.total

    def get_last_transaction(self):
        return self.last_transaction
#!/usr/bin/env python3
class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    if not isinstance(price, float) or price <= 0:
      raise ValueError("Price must be a positive number")
    if not isinstance(quantity, int) or quantity <= 0:
      raise ValueError("Quantity must be a positive integer")
    self.total += price * quantity
    self.items.append((title, price, quantity))

  def apply_discount(self):
    if not isinstance(self.discount, (int, float)) or not (0 <= self.discount <= 1):
      raise ValueError("Discount must be a number between 0 and 1 (inclusive)")
    self.total -= self.total * self.discount
    
  
  def void_last_transaction(self):
    if not self.items:
      raise IndexError("No transactions to void")
    last_item = self.items.pop()
    self.total -= last_item[1] * last_item[2]
    
  def get_last_transaction_amount(self):
    if not self.items:
      return None
    return self.items[-1][1] * self.items[-1][2]
   



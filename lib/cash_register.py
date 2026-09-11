#!/usr/bin/env python3

class CashRegister:
    """
    A CashRegister class that simulates the basic functions of a cash register.
    Supports adding items, applying discounts, and voiding transactions.
    """
    
    def __init__(self, discount=0):
        """
        Initialize a CashRegister instance.
        
        Args:
            discount (int, optional): A discount percentage (0-100). Defaults to 0.
        
        Attributes:
            discount: The discount percentage to be applied to the total.
            total: The running total of all items added.
            items: A list of all items added (including duplicates for quantities).
            previous_transactions: A list of dictionaries tracking each transaction's details.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the current discount percentage."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Set the discount percentage with validation.
        
        Args:
            value (int): The discount percentage to set.
        
        Validates that discount is an integer between 0-100 inclusive.
        Prints error message if validation fails.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0
    
    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.
        
        Args:
            item (str): The name/description of the item.
            price (float): The price of a single unit of the item.
            quantity (int, optional): The quantity of the item to add. Defaults to 1.
        
        This method:
        - Adds the total price (price * quantity) to the register's total
        - Adds the item name to the items list (once per quantity)
        - Records the transaction in previous_transactions for later reference
        """
        # Calculate total price for this transaction
        transaction_total = price * quantity
        
        # Update the running total
        self.total += transaction_total
        
        # Add item to items list, once for each quantity
        for _ in range(quantity):
            self.items.append(item)
        
        # Record the transaction for potential voiding or discounting
        transaction = {
            'item': item,
            'price': price,
            'quantity': quantity,
            'total': transaction_total
        }
        self.previous_transactions.append(transaction)
    
    def apply_discount(self):
        """
        Apply the discount percentage to the total price.
        
        This method:
        - Checks if there are any transactions to discount
        - Calculates the discount amount based on the percentage
        - Reduces the total by the discount amount
        - Removes the last transaction from previous_transactions
        - Updates the items list to reflect the removal
        - Prints a success message with the new total
        - If no discount is set or no transactions exist, prints an error message
        """
        # Check if there are transactions to apply discount to
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        
        # Get the last transaction details
        last_transaction = self.previous_transactions[-1]
        
        # Calculate the discount amount
        discount_amount = self.total * (self.discount / 100)
        
        # Apply the discount to the total
        self.total -= discount_amount
        
        # Remove the last transaction from the history
        self.previous_transactions.pop()
        
        # Remove items from the items list (reverse order to maintain consistency)
        for _ in range(last_transaction['quantity']):
            if self.items:
                self.items.pop()
        
        # Print success message with formatted total
        print(f"After the discount, the total comes to ${self.total:.2f}.")
    
    def void_last_transaction(self):
        """
        Remove the last transaction from the register.
        
        This method:
        - Checks if there are any transactions to void
        - Removes the last transaction from previous_transactions
        - Subtracts the transaction's total from the register's total
        - Removes the corresponding items from the items list
        - If no transactions exist, prints an error message
        """
        # Check if there are transactions to void
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        
        # Get the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Subtract the transaction total from the running total
        self.total -= last_transaction['total']
        
        # Remove items from the items list (in reverse to match LIFO behavior)
        for _ in range(last_transaction['quantity']):
            if self.items:
                self.items.pop()

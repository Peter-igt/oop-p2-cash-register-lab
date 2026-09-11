class CashRegister:
    def __init__(self, discount=0):
        """Initialize the cash register."""
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Return the discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Set discount between 0 and 100."""
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        """Add an item and update the total."""
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the discount to the total."""
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (1 - self.discount / 100)

        # Clear transactions so the same transaction is not discounted again.
        self.previous_transactions = []

        print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        """Remove the last transaction."""
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()

        item_total = transaction["price"] * transaction["quantity"]
        self.total -= item_total

        for _ in range(transaction["quantity"]):
            self.items.pop()

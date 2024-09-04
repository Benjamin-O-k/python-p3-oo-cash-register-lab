class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = (0, 0) #(price ,quantity)

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        self.items.extend([title] * quantity)
        self.last_transaction = (price, quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction != (0, 0):
            last_price, last_quantity = self.last_transaction
            self.total -= (last_price * last_quantity)
            for _ in range(last_quantity):
                self.items.pop()
            self.last_transaction = (0, 0)

class Book:

    def __init__(self, isbn, author, price, quantity):
        self.isbn = isbn
        self.author = author

        if price >= 0:
            self.price = price
        else:
            raise ValueError("Price cannot be negative")

        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Quantity cannot be negative")

        self.book = None
    
    def mapper_no_id(self):
        return {"isbn": self.isbn, "author": self.author, "price" : self.price, "quantity" : self.quantity}

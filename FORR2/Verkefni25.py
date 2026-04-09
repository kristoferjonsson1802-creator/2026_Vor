class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        return f"{self.title} by {self.author}"

    def check_availability(self):
        if self.copies > 0:
            return f"Copies available: {self.copies}"
        else:
            return "Sorry, this book is currently out of stock."

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            return f"You have borrowed '{self.title}'. Copies left: {self.copies}"
        else:
            return "Sorry, this book is currently out of stock."


book1 = Book("1984", "George Orwell", 3)
print(book1.check_availability())
print(book1.borrow_book())
print(book1.check_availability())

book2 = Book("House", "Jhon Oregon", 1)
print(book2.check_availability())
print(book2.borrow_book())
print(book2.borrow_book())
print(book2.check_availability())
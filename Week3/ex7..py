class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def show_books(self):
        for book in self.books:
            print(book)


lib = Library()
lib.add_book("Python Basics")
lib.add_book("Django pdf")
lib.show_books()

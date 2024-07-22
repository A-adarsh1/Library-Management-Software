class Library:
    def __init__(self, no_of_books, books: list):
        if books is None:
            books = []
        self.__no_of_books = no_of_books
        self.__books = books

    class __WrongArgumentValue(Exception):
        def __init__(self, message):
            super().__init__(message)
            self.message = message

    def books(self):
        print("Name of Books : ")
        for book in self.__books:
            print(book)

    def add_book(self, book_name):
        self.__books.append(book_name)
        self.__no_of_books += 1

    def total_books(self):
        if self.__no_of_books == len(self.__books):
            print(f"Total no. of Books : {self.__no_of_books}")
        else:
            raise self.__WrongArgumentValue("Number of books and Name of books are not Same.")


janakpur_library = Library(5, ["Seto Bagh", "Summer Love", "Laxmi prasad Devkota", "Palpasa Cafe", "Seto Dharti"])
total_books = janakpur_library.total_books()
print(total_books)
janakpur_library.books()
janakpur_library.add_book("Buddha Darshan")
print(janakpur_library.total_books())
janakpur_library.books()

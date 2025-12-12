from src.BookCollection import BookCollection
from src.BookDictCollection import IsbnBookDictCollection, AuthorBookDictCollection, YearBookDictCollection

class Library:

    def __init__(self):
        self.books = BookCollection()
        self.isbnDict = IsbnBookDictCollection()
        self.authorDict = AuthorBookDictCollection()
        self.yearDict = YearBookDictCollection()

    def getBooksByName(self, name: str) -> BookCollection:
        books: BookCollection = BookCollection()
        for book in self.books:
            if book.title == name:
                books.add(book)
        return books

    def getBooksByAuthor(self, author: str) -> BookCollection:
        books: BookCollection = BookCollection()
        for book in self.authorDict[author]:
            books.add(book)
        return books

    def getBooksByYear(self, year: int) -> BookCollection:
        books: BookCollection = BookCollection()
        for book in self.yearDict[year]:
            books.add(book)
        return books

    def getBooksByGenre(self, genre: str) -> BookCollection:
        books: BookCollection = BookCollection()
        for book in self.books:
            if book.genre == genre:
                books.add(book)
        return books

    def getBookByIsbn(self, isbn: int):
        if isbn in self.isbnDict:
            return self.isbnDict[isbn]
        raise ValueError

    def getBooksByFilters(self, *, name="", author="", year=-10000, genre="", isbn=-1) -> BookCollection:
        books: BookCollection = BookCollection()
        for book in self.books:
            approach: int = 1
            if name != "" and book.title != name:
                approach = 0

            if author != "" and book.author != author:
                approach = 0

            if year != -10000 and book.year != year:
                approach = 0

            if genre != "" and book.genre != genre:
                approach = 0

            if isbn != -1 and book.isbn != isbn:
                approach = 0

            if approach:
                books.add(book)
        return books

    def deleteBooksByName(self, name: str) -> None:
        books: BookCollection = self.getBooksByName(name)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def deleteBooksByAuthor(self, author: str) -> None:
        books: BookCollection = self.getBooksByAuthor(author)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def deleteBooksByYear(self, year: int) -> None:
        books: BookCollection = self.getBooksByYear(year)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def deleteBooksByGenre(self, genre: str) -> None:
        books: BookCollection = self.getBooksByGenre(genre)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def deleteBookByIsbn(self, isbn: int) -> None:
        book = self.getBookByIsbn(isbn)
        self.books.remove(book)
        self.authorDict.remove(book.author, book)
        self.yearDict.remove(book.year, book)
        self.isbnDict.remove(book.isbn, book)

    def deleteBooksByFilters(self, **filters) -> None:
        books: BookCollection = self.getBooksByFilters(**filters)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def addBook(self, book):
        self.books.add(book)
        self.yearDict[book.year] = book
        self.isbnDict[book.isbn] = book
        self.authorDict[book.author] = book

    def update_book(self,old_book,new_book):
        self.deleteBookByIsbn(old_book.isbn)
        self.addBook(new_book)

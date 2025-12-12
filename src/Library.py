from src.Book import Book
from src.BookCollection import BookCollection
from src.BookDictCollection import IsbnBookDictCollection, AuthorBookDictCollection, YearBookDictCollection


class Library:
    """
    класс библеотеки с книгами, в которой можно искать, добавлять, удалять, обновлять книги по isbn, автрору, году
    """

    def __init__(self):
        """
            конструктор library
        """
        self.books = BookCollection()
        self.isbnDict = IsbnBookDictCollection()
        self.authorDict = AuthorBookDictCollection()
        self.yearDict = YearBookDictCollection()

    def get_books_by_name(self, name: str) -> BookCollection:
        """
            функция для получения всех книг по имени
            :return: BookCollection c найденными книгами
        """
        books: BookCollection = BookCollection()
        for book in self.books:
            if book.title == name:
                books.add(book)
        return books

    def get_books_by_author(self, author: str) -> BookCollection:
        """
            функция для получения всех книг по имени автора
            :return: BookCollection c найденными книгами
        """
        books: BookCollection = BookCollection()
        for book in self.authorDict[author]:
            books.add(book)
        return books

    def get_books_by_year(self, year: int) -> BookCollection:
        """
            функция для получения всех книг по году выхода
            :return: BookCollection c найденными книгами
        """
        books: BookCollection = BookCollection()
        for book in self.yearDict[year]:
            books.add(book)
        return books

    def get_books_by_genre(self, genre: str) -> BookCollection:
        """
            функция для получения всех книг по жанру
            :return: BookCollection c найденными книгами
        """
        books: BookCollection = BookCollection()
        for book in self.books:
            if book.genre == genre:
                books.add(book)
        return books

    def get_book_by_isbn(self, isbn: int) -> Book:
        """
            функция для получения книги по isbn
            :return: Book
        """
        if isbn in self.isbnDict:
            return self.isbnDict[isbn]
        raise ValueError

    def get_books_by_filters(self, *, name="", author="", year=-10000, genre="", isbn=-1) -> BookCollection:
        """
            функция для получения вех книг с одинаковыми именем, годом выхода, автором, жанром, isbn
            :return: BookCollection c найденными книгами
        """
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

    def delete_books_by_name(self, name: str) -> None:
        """
            функция для удаления книг по имени
            :return: ничего не возвращает
        """
        books: BookCollection = self.get_books_by_name(name)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def delete_books_by_author(self, author: str) -> None:
        """
            функция для удаления книг по имени
            :return: ничего не возвращает
        """
        books: BookCollection = self.get_books_by_author(author)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def delete_books_by_year(self, year: int) -> None:
        """
            функция для удаления книг по году выхода
            :return: ничего не возвращает
        """
        books: BookCollection = self.get_books_by_year(year)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def delete_books_by_genre(self, genre: str) -> None:
        """
            функция для удаления книг по жанру
            :return: ничего не возвращает
        """
        books: BookCollection = self.get_books_by_genre(genre)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def delete_book_by_isbn(self, isbn: int) -> None:
        """
            функция для удаления книги по isbn
            :return: ничего не возвращает
        """
        book = self.get_book_by_isbn(isbn)
        self.books.remove(book)
        self.authorDict.remove(book.author, book)
        self.yearDict.remove(book.year, book)
        self.isbnDict.remove(book.isbn, book)

    def delete_books_by_filters(self, **filters) -> None:
        """
            функция для удаления книг по жанру,имени,автору,году,isbn
            :return: ничего не возвращает
        """
        books: BookCollection = self.get_books_by_filters(**filters)
        for book in books:
            self.books.remove(book)
            self.authorDict.remove(book.author, book)
            self.yearDict.remove(book.year, book)
            self.isbnDict.remove(book.isbn, book)

    def add_book(self, book: Book) -> None:
        """
            функция для добавления книги в библиотеку
            :return: ничего не возвращает
        """
        self.books.add(book)
        self.yearDict[book.year] = book
        self.isbnDict[book.isbn] = book
        self.authorDict[book.author] = book

    def update_book(self, old_book: Book, new_book: Book) -> None:
        """
            функция для обновления книги в библиотеке
            :return: ничего не возвращает
        """
        self.delete_book_by_isbn(old_book.isbn)
        self.add_book(new_book)

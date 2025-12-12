from src.Book import Book


def test_book():
    """
        Тесты для Book
    """
    book:Book = Book("title","author",2025,"genre",1111111111)
    Book.title == "1"
    Book.author == "1"
    Book.year == 1
    Book.genre == "1"
    Book.isbn == 1

    assert book.title == "title"
    assert book.author == "author"
    assert book.year == 2025
    assert book.genre == "genre"
    assert book.isbn == 1111111111

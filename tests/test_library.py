from src.Book import Book
from src.Library import Library


def test_library():
    """
        Тесты для library
    """
    lib: Library = Library()
    book1: Book = Book("Title1", "Author1", 2000, "Genre1", 123456789)
    book2: Book = Book("Title1", "Author1", 2000, "Genre2", 987654321)
    book3: Book = Book("Title3", "Author2", 2001, "Genre3", 987654322)

    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)

    assert len(lib.get_books_by_author(book1.author)) == 2
    assert len(lib.get_books_by_name(book1.title)) == 2
    assert len(lib.get_books_by_genre(book1.genre)) == 1
    assert len(lib.get_books_by_filters(genre=book1.genre)) == 1
    assert len(lib.get_books_by_filters(name=book1.title)) == 2
    assert lib.get_book_by_isbn(book1.isbn).isbn == book1.isbn

    book4: Book = Book("Title3", "Author3", 2001, "Genre3", 987654322)

    lib.update_book(book3, book4)

    assert lib.get_book_by_isbn(book3.isbn).author == book4.author
    lib.delete_book_by_isbn(book4.isbn)

    try:
        lib.get_book_by_isbn(book3.isbn)
        assert 0 == 1
    except Exception:
        assert 1 == 1

    lib.delete_books_by_name(book1.title)
    assert len(lib.get_books_by_name(book1.title)) == 0
    lib.add_book(book1)
    lib.add_book(book2)
    lib.delete_books_by_year(book1.year)
    assert len(lib.get_books_by_year(book1.year)) == 0
    lib.add_book(book1)
    lib.add_book(book2)
    lib.delete_books_by_author(book1.author)
    assert len(lib.get_books_by_author(book1.author)) == 0
    lib.delete_books_by_genre(book2.genre)
    assert len(lib.get_books_by_genre(book2.genre)) == 0
    lib.add_book(book1)
    lib.delete_books_by_filters(name=book1.title)
    assert len(lib.get_books_by_name(book1.title)) == 0

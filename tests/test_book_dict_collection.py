from src.Book import Book
from src.BookDictCollection import YearBookDictCollection, IsbnBookDictCollection, AuthorBookDictCollection


def test_book_dict_collection():
    """
        Тесты для BookDictCollections
    """
    year_collection:YearBookDictCollection = YearBookDictCollection()
    isbn_collection:IsbnBookDictCollection = IsbnBookDictCollection()
    author_collection:AuthorBookDictCollection = AuthorBookDictCollection()

    book1:Book = Book("Title1", "Author1", 2000, "Genre1",123456789)
    book2:Book = Book("Title2", "Author1", 2000, "Genre2" ,987654321)
    book3:Book = Book("Title3", "Author2", 2001, "Genre3" ,987654322)

    year_collection[book1.year]=book1
    year_collection[book2.year]=book2
    year_collection[book3.year]=book3

    isbn_collection[book1.isbn]=book1
    isbn_collection[book2.isbn]=book2
    isbn_collection[book3.isbn]=book3

    author_collection[book1.author]=book1
    author_collection[book2.author]=book2
    author_collection[book3.author]=book3

    assert len(year_collection)==2
    assert len(isbn_collection)==3
    assert len(author_collection)==2

    year_collection.remove(book1.year,book1)
    isbn_collection.remove(book1.isbn,book1)
    author_collection.remove(book1.author,book1)

    assert len(year_collection)==2
    assert len(isbn_collection)==2
    assert len(author_collection)==2

    test_contain1:bool = book1 in year_collection
    test_contain2:bool = book1.isbn in isbn_collection
    test_contain3:bool = book1 in author_collection

    assert test_contain1==0
    assert test_contain2==0
    assert test_contain3==0

    assert year_collection[book2.year]==[book2]
    assert isbn_collection[book2.isbn]==book2
    assert author_collection[book2.author]==[book2]

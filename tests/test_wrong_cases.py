from src.Book import Book
from src.BookCollection import BookCollection
from src.BookDictCollection import YearBookDictCollection, IsbnBookDictCollection, AuthorBookDictCollection


def test_wrong_cases():
    """
        тесты с ошибочными данными
    """

    collection: BookCollection = BookCollection()
    year_collection:YearBookDictCollection = YearBookDictCollection()
    isbn_collection:IsbnBookDictCollection = IsbnBookDictCollection()
    author_collection:AuthorBookDictCollection = AuthorBookDictCollection()

    try:
        collection[0]
        assert 0==1
    except Exception:
        assert 1==1

    try:
        collection.remove(Book("","",0,"",0))
        assert 0==1
    except Exception:
        assert 1==1

    try:
        collection[:]
        assert 0==1
    except Exception:
        assert 1==1

    try:
        year_collection[0]
        assert 0==1
    except Exception:
        assert 1==1

    try:
        author_collection[""]
        assert 0==1
    except Exception:
        assert 1==1

    try:
        isbn_collection[1]
        assert 0==1
    except Exception:
        assert 1==1

    try:
        year_collection.remove(0,Book("","",0,"",0))
        assert 0==1
    except Exception:
        assert 1==1

    try:
        author_collection.remove("",Book("","",0,"",0))
        assert 0==1
    except Exception:
        assert 1==1

    try:
        isbn_collection.remove(0,Book("","",0,"",0))
        assert 0==1
    except Exception:
        assert 1==1

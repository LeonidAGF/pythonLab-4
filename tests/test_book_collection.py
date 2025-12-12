from src.Book import Book
from src.BookCollection import BookCollection


def test_book_collection():
    """
        Тесты для bookCollection
    """

    collection:BookCollection = BookCollection()
    assert len(collection)==0
    collection.add(Book("1","1",1949,"",123))
    collection.add(Book("2","2",1929,"",122))

    assert collection[0].title=="1"
    assert len(collection)==2
    collection[0] = Book("3","3",1929,"",122)
    assert collection[0].title=="3"
    assert len(collection)==2
    new_collection:BookCollection = collection[:]
    assert len(new_collection) == 2
    collection.remove(collection[0])
    assert len(collection) == 1
    test_contain:bool = collection[0] in collection
    assert test_contain==1

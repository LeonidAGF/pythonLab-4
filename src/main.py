from src.Book import Book
from src.BookDictCollection import YearBookDictCollection
from src.simulation import run_simulation


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    """
    s = BookCollection()
    s.add(Book("1","1",1949,"",123))
    s.add(Book("2","2",1929,"",122))

    print(s[0].title)

    s[0] = Book("3","3",1929,"",122)

    print(s[0].title)

    print(len(s))
    print(s[:])
    s.remove(s[0])
    print(len(s))
    """

    collection = YearBookDictCollection()

    book1 = Book("Title1", "Author1", 2000, "Genre1",123456789)
    book2 = Book("Title2", "Author1", 2000, "Genre2" ,987654321)

    collection[book1.year]=book1
    collection[book2.year]=book2

    print(len(collection))

    collection.remove(book1.year,book1)
    print(book1 in collection)


    print(len(collection))
    print(collection[book2.year])
    run_simulation(500)

if __name__ == "__main__":
    main()

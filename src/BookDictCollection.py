from src.Book import Book


class BookDictCollection:
    """
    Базовый класс для BookDict
    """

    def __init__(self):
        """
        конструктор
        """
        self.data = {}

    def remove(self, index, el) -> None:
        """
        функция удаления элемента по некоторому ключу
        :return: Данная функция ничего не возвращает
        """
        if self.data.get(index) == el:
            del self.data[index]
        else:
            raise ValueError

    def __getitem__(self, index):
        """
          функция получения элемента по некоторому ключу
          :return: найденный элемент
        """
        return self.data[index]

    def __setitem__(self, index, book: Book) -> None:
        """
        дабавление нового элемента по ключу
        :return: Данная функция ничего не возвращает
        """
        self.data[index] = book

    def __iter__(self):
        """
           получение коллекции для итерирования
          :return: dict
        """
        return self.data.values()

    def __len__(self) -> int:
        """
          получение количества ключей
          :return: количество ключей
        """
        return len(self.data)

    def __contains__(self, book: Book) -> bool:
        """
          функция проверяющая содержание элемента в коллекции
          :return: true если элемент содержится в коллекции и false иначе
        """
        for key in self.data:
            if self.data.get(key) == book:
                return True
        return False


class IsbnBookDictCollection(BookDictCollection):
    """
      коллекция сортирующая книги по isbn
    """

    def __contains__(self, isbn) -> bool:
        """
          функция проверяющая содержание isbn в коллекции
          :return: true если элемент содержится в коллекции и false иначе
        """
        for key in self.data:
            if self.data.get(key).isbn == isbn:
                return True
        return False


class AuthorBookDictCollection(BookDictCollection):
    """
        Коллекция сортирующая книги по именам авторов
    """

    def remove(self, author: str, el) -> None:
        """
        функция удаления элемента по некоторому ключу
        :return: Данная функция ничего не возвращает
        """
        if el in self.data[author]:
            self.data[author].remove(el)
            if len(self.data[author]) == 0:
                del self.data[author]

    def __setitem__(self, index: str, book: Book) -> None:
        """
        дабавление нового элемента по ключу
        :return: Данная функция ничего не возвращает
        """
        if index not in self.data:
            self.data[index] = []
        self.data[index].append(book)

    def __getitem__(self, index):
        """
          функция получения элемента по некоторому ключу
          :return: найденный элемент
        """
        if index not in self.data:
            return []
        return self.data[index]

    def __contains__(self, book: Book) -> bool:
        """
            функция проверяющая содержание элемента в коллекции
            :return: true если элемент содержится в коллекции и false иначе
        """
        for key in self.data:
            if book in self.data.get(key):
                return True
        return False


class YearBookDictCollection(BookDictCollection):
    """
        Коллекция сортирующая книги по годам
    """

    def remove(self, year, book: Book) -> None:
        """
        функция удаления элемента по некоторому ключу
        :return: Данная функция ничего не возвращает
        """
        if book in self.data[year]:
            self.data[year].remove(book)
            if len(self.data[year]) == 0:
                del self.data[year]

    def __setitem__(self, index: int, book: Book) -> None:
        """
        дабавление нового элемента по ключу
        :return: Данная функция ничего не возвращает
        """
        if index not in self.data:
            self.data[index] = []
        self.data[index].append(book)

    def __getitem__(self, index):
        """
          функция получения элемента по некоторому ключу
          :return: найденный элемент
        """
        if index not in self.data:
            return []
        return self.data[index]

    def __contains__(self, book: Book) -> bool:
        """
          функция проверяющая содержание элемента в коллекции
          :return: true если элемент содержится в коллекции и false иначе
        """
        for key in self.data:
            if book in self.data.get(key):
                return True
        return False

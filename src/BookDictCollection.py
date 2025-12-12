from collections import defaultdict


class BookDictCollection:
    """
    Базовый класс для индекса книг.
    Определяет интерфейс для добавления, удаления и поиска книг.
    """

    def __init__(self):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.data = {}

    def remove(self, index, el) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if self.data.get(index) == el:
            del self.data[index]
        else:
            raise ValueError

    def __getitem__(self, index):
        """
          Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
          :return: Данная функция ничего не возвращает
        """
        return self.data[index]

    def __setitem__(self, index, book) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.data[index] = book

    def __iter__(self):
        """
          Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
          :return: Данная функция ничего не возвращает
        """
        return iter(self.data.values())

    def __len__(self):
        """
          Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
          :return: Данная функция ничего не возвращает
        """
        return len(self.data)

    def __contains__(self, book):
        """
          Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
          :return: Данная функция ничего не возвращает
        """
        for key in self.data:
            if self.data.get(key) == book:
                return True
        return False


class IsbnBookDictCollection(BookDictCollection):
    """
      Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
      :return: Данная функция ничего не возвращает
    """
    def __contains__(self, isbn:int):
        """
          Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
          :return: Данная функция ничего не возвращает
        """
        for key in self.data:
            if self.data.get(key).isbn == isbn:
                return True
        return False


class AuthorBookDictCollection(BookDictCollection):
    """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
    """

    def __init__(self):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        super().__init__()
        self.data = defaultdict(list)

    def remove(self, author: str, el) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if el in self.data[author]:
            self.data[author].remove(el)
            if not self.data[author]:
                del self.data[author]

    def __setitem__(self, index, book) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.data[index].append(book)

    def __contains__(self, book):
        """
          Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
          :return: Данная функция ничего не возвращает
        """
        for key in self.data:
            if book in self.data.get(key):
                return True
        return False


class YearBookDictCollection(BookDictCollection):
    """
      Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
      :return: Данная функция ничего не возвращает
    """

    def __init__(self):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        super().__init__()
        self.data = defaultdict(list)

    def remove(self, year, book):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if book in self.data[year]:
            self.data[year].remove(book)
            if not self.data[year]:
                del self.data[year]

    def __setitem__(self, index, book) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.data[index].append(book)

    def __contains__(self, book):
        """
          Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
          :return: Данная функция ничего не возвращает
        """
        for key in self.data:
            if book in self.data.get(key):
                return True
        return False

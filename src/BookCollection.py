from src.Book import Book


class BookCollection:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    def __init__(self) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.list: list[Book] = []

    def __getitem__(self, index: int):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        #if index >= len(self.list) or index < 0:
        #    raise ValueError
        return self.list[index]

    def add(self, book) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.list.append(book)

    def __setitem__(self, index: int, book) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if index >= len(self.list) or index < 0:
            raise ValueError
        self.list[index] = book

    def remove(self, book) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        try:
            self.list.remove(book)
        except Exception as e:
            raise e

    def __iter__(self):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        for el in self.list:
            yield el

    def __len__(self) -> int:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        return len(self.list)

    def __contains__(self, book) -> bool:
        return book in self.list

from src.Book import Book


class BookCollection:
    """
    коллекция книг
    """

    def __init__(self) -> None:
        """
        конструктор BookCollection
        """
        self.list: list[Book] = []

    def __getitem__(self, index):
        """
        получение книги по индексу или через срез
        :return: найденная книга или срез
        """
        try:
            return self.list[index]
        except Exception:
            raise ValueError

    def add(self, book: Book) -> None:
        """
        функция добовления книги в конец спмска
        :return: Данная функция ничего не возвращает
        """
        self.list.append(book)

    def __setitem__(self, index: int, book: Book) -> None:
        """
        функция устанавлявающая книгу в определённое место списка по index
        :return: Данная функция ничего не возвращает
        """
        if index >= len(self.list) or index < 0:
            raise ValueError
        self.list[index] = book

    def remove(self, book: Book) -> None:
        """
        Функция удаляющая из списка книгу
        :return: Данная функция ничего не возвращает
        """
        try:
            self.list.remove(book)
        except Exception as e:
            raise e

    def __iter__(self):
        """
        функция позволяющая получить все элементы мвссива в цикле
        :return: book
        """
        for el in self.list:
            yield el

    def __len__(self) -> int:
        """
        функция для нахождения количества всех элементов
        :return: количество всех элементов
        """
        return len(self.list)

    def __contains__(self, book: Book) -> bool:
        """
            функция для роверки нахождения книги в колекуии
            :return: true если книга в колекции, иначе false
        """
        return book in self.list

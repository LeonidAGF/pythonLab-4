from src.Book import Book
from src.Library import Library
import random


def get_new_isbn() -> int:
    """
    функция для генерации isbn
    :return: новый isbn
    """
    return random.randint(10000000000, 99999999999)


def get_new_year():
    """
    функция для генерации года
    :return: новый год
    """
    return random.randint(2000, 2025)


def get_new_str():
    """
    функция для генерации какой-то строки
    :return: новую строку
    """
    title = ""
    len = random.randint(5, 25)
    for i in range(len):
        sym = chr(random.randint(97, 122))
        title += sym
    return title


def run_simulation(steps: int = 20, seed: int | None = None) -> int:
    """
    функция симуляции. Есть 6 событий: поиск книг, удаление книг, попытка получить не существующую книгу, обновление книг,добовление книг, пожар.
    :return: 0 если симуляция закончилась успешно или 1 если проихошла ошибка
    """
    try:
        random.seed(None)
        if seed is not None:
            random.seed(seed)

        lib = Library()

        titles: list[str] = []
        genres: list[str] = []
        authors: list[str] = []
        years: list[int] = []
        isbns: list[int] = []

        for i in range(5000):
            title: str = get_new_str()
            genre: str = get_new_str()
            author: str = get_new_str()
            year: int = get_new_year()
            titles.append(title)
            genres.append(genre)
            authors.append(author)
            years.append(year)

        for i in range(10000):
            title_book: str = titles[random.randint(0, len(titles) - 1)]
            genre_book: str = genres[random.randint(0, len(genres) - 1)]
            author_book: str = authors[random.randint(0, len(authors) - 1)]
            year_book: int = years[random.randint(0, len(years) - 1)]
            isbn_book: int = get_new_isbn()
            isbns.append(isbn_book)

            lib.add_book(Book(title_book, author_book, year_book, genre_book, isbn_book))

        for j in range(steps):

            event_code: int = random.randint(1, 6)

            match event_code:
                case 1:
                    # add book
                    book_title: str = get_new_str()
                    book_genre: str = get_new_str()
                    book_author: str = get_new_str()
                    book_year: int = get_new_year()
                    book_isbn: int = get_new_isbn()
                    titles.append(book_title)
                    genres.append(book_genre)
                    authors.append(book_author)
                    years.append(book_year)
                    isbns.append(book_isbn)

                    lib.add_book(Book(book_title, book_author, book_year, book_genre, book_isbn))
                    print("new book added")
                case 2:
                    try:
                        # delete_book
                        delete_event_code: int = random.randint(1, 5)
                        if delete_event_code == 1:
                            # delete by title
                            titile_num_delete: int = random.randint(0, len(titles) - 1)
                            lib.delete_books_by_name(titles[titile_num_delete])
                        elif delete_event_code == 2:
                            # delete by author
                            author_num_delete: int = random.randint(0, len(authors) - 1)
                            lib.delete_books_by_author(authors[author_num_delete])
                        elif delete_event_code == 3:
                            # delete by year
                            year_num_delete: int = random.randint(0, len(years) - 1)
                            lib.delete_books_by_year(years[year_num_delete])
                        elif delete_event_code == 4:
                            # delete by genre
                            genre_num_delete: int = random.randint(0, len(genres) - 1)
                            lib.delete_books_by_genre(genres[genre_num_delete])
                        else:
                            # delete by isbn
                            isbn_num_delete: int = random.randint(0, len(isbns) - 1)
                            lib.delete_book_by_isbn(isbns[isbn_num_delete])
                    except ValueError:
                        print("Coosen book/books to delete have already deleted")
                    print("book deleted")
                case 3:
                    # search_book
                    try:
                        search_event_code: int = random.randint(1, 6)
                        if search_event_code == 1:
                            # search by title
                            titile_num_search: int = random.randint(0, len(titles) - 1)
                            lib.get_books_by_name(titles[titile_num_search])
                        elif search_event_code == 2:
                            # search by author
                            author_num_search: int = random.randint(0, len(authors) - 1)
                            lib.get_books_by_author(authors[author_num_search])
                        elif search_event_code == 3:
                            # search by year
                            year_num_search: int = random.randint(0, len(years) - 1)
                            lib.get_books_by_year(years[year_num_search])
                        elif search_event_code == 4:
                            # search by genre
                            genre_num_search: int = random.randint(0, len(genres) - 1)
                            lib.get_books_by_genre(genres[genre_num_search])
                        else:
                            # search by isbn
                            isbn_num_search: int = random.randint(0, len(isbns) - 1)
                            lib.get_book_by_isbn(isbns[isbn_num_search])
                    except ValueError:
                        print("Coosen book/books to search have already deleted")
                    print("book searched")
                case 4:
                    # update_book
                    try:
                        update_search_event_code: int = random.randint(1, 6)
                        if update_search_event_code == 1:
                            # search by title
                            titile_num_update: int = random.randint(0, len(titles) - 1)
                            collection_upadte = lib.get_books_by_name(titles[titile_num_update])
                            for el in collection_upadte:
                                new_book_update: Book = Book(el.title, el.author, el.year, el.genre, el.isbn)
                                new_book_update.title = titles[random.randint(0, len(titles) - 1)]
                                new_book_update.genre = genres[random.randint(0, len(genres) - 1)]
                                lib.update_book(el, new_book_update)
                        elif update_search_event_code == 2:
                            # search by author
                            author_num_update: int = random.randint(0, len(authors) - 1)
                            collection_upadte_author = lib.get_books_by_author(authors[author_num_update])
                            for el in collection_upadte_author:
                                new_book_update_author: Book = Book(el.title, el.author, el.year, el.genre, el.isbn)
                                new_book_update_author.title = titles[random.randint(0, len(titles) - 1)]
                                new_book_update_author.genre = genres[random.randint(0, len(genres) - 1)]
                                lib.update_book(el, new_book_update_author)
                        elif update_search_event_code == 3:
                            # search by year
                            year_num_upadate: int = random.randint(0, len(years) - 1)
                            collection_upadte_year = lib.get_books_by_year(years[year_num_upadate])
                            for el in collection_upadte_year:
                                new_book_update_year: Book = Book(el.title, el.author, el.year, el.genre, el.isbn)
                                new_book_update_year.title = titles[random.randint(0, len(titles) - 1)]
                                new_book_update_year.genre = genres[random.randint(0, len(genres) - 1)]
                                lib.update_book(el, new_book_update_year)
                        elif update_search_event_code == 4:
                            # search by genre
                            genre_num_update: int = random.randint(0, len(genres) - 1)
                            collection_upadte_genre = lib.get_books_by_genre(genres[genre_num_update])
                            for el in collection_upadte_genre:
                                new_book_update_genre: Book = Book(el.title, el.author, el.year, el.genre, el.isbn)
                                new_book_update_genre.title = titles[random.randint(0, len(titles) - 1)]
                                new_book_update_genre.genre = genres[random.randint(0, len(genres) - 1)]
                                lib.update_book(el, new_book_update_genre)
                        else:
                            # search by isbn
                            isbn_num_update: int = random.randint(0, len(isbns) - 1)
                            old_book: Book = lib.get_book_by_isbn(isbns[isbn_num_update])
                            new_book_update_isbn: Book = Book(old_book.title, old_book.author, old_book.year,
                                                              old_book.genre, old_book.isbn)
                            new_book_update_isbn.title = titles[random.randint(0, len(titles) - 1)]
                            new_book_update_isbn.genre = genres[random.randint(0, len(genres) - 1)]
                            lib.update_book(old_book, new_book_update_isbn)

                    except ValueError:
                        print("Coosen book/books to update have already deleted")

                    print("book updated")
                case 5:
                    # receiving a non-existent book
                    not_existed_isbn: int = get_new_isbn()
                    if not_existed_isbn in isbns:
                        not_existed_isbn = get_new_isbn()

                    try:
                        lib.get_book_by_isbn(not_existed_isbn)
                        print("receiving a non-existent book")
                    except Exception:
                        print("cant recive a non-existent book")

                case 6:
                    # born_library
                    scale: int = random.randint(1, 100)
                    for t in range(scale):
                        try:
                            delete_event_code_simulation_fire: int = random.randint(1, 5)
                            if delete_event_code_simulation_fire == 1:
                                # delete by title
                                titile_num_simulation_fire: int = random.randint(0, len(titles) - 1)
                                lib.delete_books_by_name(titles[titile_num_simulation_fire])
                            elif delete_event_code_simulation_fire == 2:
                                # delete by author
                                author_num_simulation_fire: int = random.randint(0, len(authors) - 1)
                                lib.delete_books_by_author(authors[author_num_simulation_fire])
                            elif delete_event_code_simulation_fire == 3:
                                # delete by year
                                year_num_simulation_fire: int = random.randint(0, len(years) - 1)
                                lib.delete_books_by_year(years[year_num_simulation_fire])
                            elif delete_event_code_simulation_fire == 4:
                                # delete by genre
                                genre_num_simulation_fire: int = random.randint(0, len(genres) - 1)
                                lib.delete_books_by_genre(genres[genre_num_simulation_fire])
                            else:
                                # delete by isbn
                                isbn_num_simulation_fire: int = random.randint(0, len(isbns) - 1)
                                lib.delete_book_by_isbn(isbns[isbn_num_simulation_fire])
                        except ValueError:
                            print("This book/books have already born")
                    print("fire!!!")
        print("end")
        return 0
    except Exception as e:
        print(e)
        return 1

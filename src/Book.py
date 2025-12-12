class Book:
    """
    класс книги
    """
    title:str = ""
    author:str = ""
    year:int = 0
    genre:str = ""
    isbn:int = 0

    def __init__(self,title:str,author:str,year:int,genre:str,isbn:int):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

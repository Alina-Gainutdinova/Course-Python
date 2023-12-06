class Library:
    def __init__(self) -> None:
        self.books = ['Anna Karenina', 'Война и мир', 'Harry Potter',
                      'Оно', 'Atomic habits', 'Sherlok Holms', 'Таинственный остров',
                      'Эмоциональный интеллект', 'Не ссы', 'Психология влияния']

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book}" добавлена в библиотеку')

    def find_book(self, book):
        print(f'Книга "{book}" найдена') if book in self.books else print(
            f'Книга "{book}" не найдена')


book_1 = Library()
book_1.add_book('Romeo and Juletta')
book_1.find_book('Anna Karenina')
book_1.find_book('Stiven King')
book_1.find_book('Python')
book_1.add_book('Метрвые души')

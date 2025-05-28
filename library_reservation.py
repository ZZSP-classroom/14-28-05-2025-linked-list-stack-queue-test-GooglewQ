class Book:
    def __init__(self,user_name,book_title) -> None:
        self.user_name = user_name
        self.book_title = book_title

class Queue:
    def __init__(self) -> None:
        self.list = []

    def enqueue(self,book):
        self.list.append(book)

    def dequeue(self):
        self.list.pop(0)

    def peek(self):
        print(self.list[0].user_name)
        print(self.list[0].book_title)
        return self.list[0]
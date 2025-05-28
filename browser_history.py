class URL():
    def __init__(self,link) -> None:
        self.link = link

class Stack():
    def __init__(self) -> None:
        self.slist = []

    def push(self,link:URL):
        self.slist.append(link)
    
    def pop(self):
        self.slist.pop()

    def peek(self):
        return self.slist[len(self.slist) - 1]

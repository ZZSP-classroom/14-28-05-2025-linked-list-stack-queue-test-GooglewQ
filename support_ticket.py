class Ticket():
    def __init__(self,ticket_id,issue_description) -> None:
        self.ticket_id = ticket_id
        self.issue_description = issue_description

class Queue:
    def __init__(self) -> None:
        self.list = []

    def enqueue(self,ticket):
        self.list.append(ticket)

    def dequeue(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]
    
    
class Stack():
    def __init__(self) -> None:
        self.slist = []

    def push(self,recevied):
        self.slist.append(recevied)
    
    def pop(self):
        self.slist.pop()

    def peek(self):
        return self.slist[len(self.slist) - 1]
    


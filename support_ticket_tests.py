import unittest
from support_ticket import *

class supportTest(unittest.TestCase):
    def testEnqueueForProceed(self):
        q = Queue()
        tq = Queue()
        ticket = Ticket(1,"issue")
        q.enqueue(ticket)

        self.assertNotEqual(q.list,tq.list)

    def testAddingToStack(self):
        q = Queue()
        s = Stack()
        ts = Stack()
        ticket = Ticket(1,"issue")
        q.enqueue(ticket)
        s.push(q.dequeue())
        self.assertNotEqual(s.slist,ts.slist)
    
    def testRemovingFromStack(self):
        q = Queue()
        s = Stack()
        tq = Queue()
        ts = Stack()
        ticket = Ticket(1,"issue")
        q.enqueue(ticket)
        tq.enqueue(ticket)
        s.push(q.dequeue())
        ts.push(tq.dequeue())
        s.pop()
        self.assertNotEqual(s.slist,ts.slist)
    
if __name__ == "__main__":
    unittest.main()

import unittest
from library_reservation import *
class LibraryTests(unittest.TestCase):
    def testEnqueue(self):
        book = Book("Adam","Harry Potter")
        temp = []
        q = Queue()
        q.enqueue(book)

        self.assertNotEqual(temp,q.list)

    def testDequeue(self):
        book = Book("Adam","Harry Potter")
        temp = []
        temp.append(book)
        q = Queue()
        q.enqueue(book)
        q.dequeue()

        self.assertNotEqual(temp,q.list)

    def testPeek(self):
        book = Book("Adam","Harry Potter")
        q = Queue()
        q.enqueue(book)

        self.assertEqual(q.peek(),book)

if __name__ == "__main__":
    unittest.main()
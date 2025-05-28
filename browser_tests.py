import unittest 
from browser_history import *

class BrowserTests(unittest.TestCase):
    def testPush(self):
        s = Stack()
        temp = Stack()

        u = URL("https/what")
        s.push(u)
        self.assertNotEqual(s.slist,temp.slist)

    def testPop(self):
        s = Stack()
        temp = Stack()

        u = URL("https/what")
        s.push(u)
        temp.push(u)
        s.pop()

        self.assertNotEqual(s.slist,temp.slist)

    def testPeek(self):
        s = Stack()

        u = URL("https/what")
        s.push(u)

        self.assertEqual(s.peek(),u)
        
if __name__ == "__main__":
    unittest.main()
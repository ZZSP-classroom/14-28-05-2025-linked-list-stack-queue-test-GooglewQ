import unittest
from playlist_manager import *

class PlaylistTests(unittest.TestCase):
    def testAddSong(self):
        ll = LinkedList()
        templl = LinkedList()
        ll.add_song("Chicken","Jack Black")
        self.assertNotEqual(ll.sizeOfLL(),templl.sizeOfLL())

    def testRemoveSong(self):
        ll = LinkedList()
        ll.add_song("Chicken","Jack Black")
        ll.add_song("song2","artist")
        temp = ll.sizeOfLL()
        ll.remove_song()
        self.assertNotEqual(ll.sizeOfLL(),temp)

    def testRemoveSong(self):
        ll = LinkedList()
        ll.add_song("Chicken","Jack Black")
        ll.add_song("song2","artist")
        temp = ll.sizeOfLL()
        ll.remove_song()
        self.assertNotEqual(ll.sizeOfLL(),temp)

    def testGetNextSong(self):
        ll = LinkedList()
        ll.add_song("Chicken","Jack Black")
        ll.add_song("song2","artist")
        ll.add_song("Dungeon","author")
        self.assertEqual(ll.get_next_song("Chicken"),"song2")

if __name__ == "__main__":
    unittest.main()
import unittest
from FrameList import FrameList, Frame

class TestFrameListMethods(unittest.TestCase):
    def setUp(self):
        e = Frame(cargo = "eee")
        self.FrameList = FrameList(e)
        (a, b, c, d) = (Frame(cargo = "aaa"), Frame(cargo = "bbb"), Frame(cargo = "ccc"), Frame(cargo = "ddd"))
        self.Frames = [a, b, c, d]
        self.downFrame = e
        
    def test_add_last(self):
        self.FrameList.add_last(self.Frames[0])
        self.assertEqual(self.FrameList.lenght(), 1)
        self.assertEqual(str(self.FrameList.head()), "aaa")
        for i in range(1, len(self.Frames)):
            self.FrameList.add_last(self.Frames[i])
        self.assertEqual(self.FrameList.lenght(), 4)
        self.assertEqual(str(self.FrameList.head()), "aaa")
        self.assertEqual(str(self.FrameList.tail_end()), "ddd")
        for Frame in self.Frames:
            self.assertEqual(str(Frame.down()), "eee")
        
if __name__ == "__main__":
    unittest.main()
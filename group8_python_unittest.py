import unittest

class TestMyProgram(unittest.TestCase):
    def test_Total(self):
        self.assertEqual(prog.totaldata_top2,15993497)
    def test_Mean(self):
        self.assertEqual(prog.mean,5331165.67)
import unittest
import sys
import gcd

class TestGCD(unittest.TestCase):
	def test_compare(self):
		with open("requirements.txt") as text:
			for line in text:
				string = line.split(" ") 
				self.assertEqual(gcd.gcd(int(string[0]),int(string[1])), int(string[2]))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGCD('test_compare'))
    return suite

runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
test_suite = test_suite()
runner.run(test_suite)
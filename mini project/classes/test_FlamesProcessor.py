import FlamesProcessor as f
import unittest

#run using "python -m unittest"

class TestFlamesProcessor(unittest.TestCase):
	#test whether the expected output is got
	def test_result(self):
		flame = f.FlameProcessor()
		flame.callFlow_of_Methods("vimal","kavin")
		self.assertEqual(flame.result[0],"Enemy")
		flame.callFlow_of_Methods("ajay","vijay")
		self.assertEqual(flame.result[0],"Friends")		
		flame.callFlow_of_Methods("MATT","DENISE")
		self.assertEqual(flame.result[0],"Love")
		flame.callFlow_of_Methods("kishore samuthiram","deepthi")
		self.assertEqual(flame.result[0],"Affection")

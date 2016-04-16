import analysis
import unittest

class AnalysisTest(unittest.TestCase):
	def test_correct1(self):
		given_list = [1, 2, 3]
		press_list = [1, 2, 3]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": True, "hits": 3, "substitutions": 0, "additions": 0, "order error": False}))

	def test_correct2(self):
		given_list = [1, 2, 3]
		press_list = []

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 0, "substitutions": 0, "additions": 0, "order error": False}))

	def test_correct3(self):
		given_list = [1, 2, 3]
		press_list = [5, 6, 7]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 0, "substitutions": 3, "additions": 0, "order error": False}))

	def test_correct4(self):
		given_list = [1]
		press_list = [2, 1]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 1, "substitutions": 0, "additions": 1, "order error": False}))

	def test_correct5(self):
		given_list = [1, 2]
		press_list = [1, 4, 2]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 2, "substitutions": 0, "additions": 1, "order error": False}))

	def test_correct6(self):
		given_list = [1, 2, 3]
		press_list = [1, 4, 3]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 2, "substitutions": 1, "additions": 0, "order error": False}))

	def test_correct7(self):
		given_list = [1, 2, 3]
		press_list = [1, 4, 2]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 2, "substitutions": 1, "additions": 0, "order error": False}))

	def test_correct8(self):
		given_list = [1, 2, 3]
		press_list = [1, 5, 5, 2]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 2, "substitutions": 1, "additions": 1, "order error": False}))

	def test_correct9(self):
		given_list = [1, 2, 3]
		press_list = [3, 2, 3, 2, 3]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 2, "substitutions": 1, "additions": 2, "order error": False}))

	def test_correct10(self):
		given_list = [1, 2, 3, 4]
		press_list = [1, 1, 2, 4]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 3, "substitutions": 1, "additions": 0, "order error": False}))

	def test_correct11(self):
		given_list = [1, 2, 3, 4]
		press_list = [1, 1, 2, 2, 4]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 3, "substitutions": 1, "additions": 1, "order error": False}))


	def test_correct12(self):
		given_list = [1, 2, 3]
		press_list = [1, 2, 2, 3]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 3, "substitutions": 0, "additions": 1, "order error": False}))

	def test_correct13(self):
		given_list = [1, 2, 3]
		press_list = [1, 2, 1, 3]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 3, "substitutions": 0, "additions": 1, "order error": False}))

	def test_correct14(self):
		given_list = [1, 2, 3]
		press_list = [3, 2, 1]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 3, "substitutions": 0, "additions": 0, "order error": True}))

	def test_correct15(self):
		given_list = [1, 2, 3]
		press_list = [1, 3, 1, 2]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 3, "substitutions": 0, "additions": 1, "order error": True}))

	def test_correct16(self):
		given_list = [1, 2, 3]
		press_list = [3, 1]

		results = analysis.analyze_trial(given_list, press_list)
		self.assertEqual(results, ({"correct": False, "hits": 2, "substitutions": 0, "additions": 0, "order error": True}))
		
if __name__ == '__main__':
	unittest.main()
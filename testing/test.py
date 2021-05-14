import unittest
import unittest 
import script

class TestMain(unittest.TestCase):
  def test_do_stuff(self):
    test_param = 10
    result = script.do_stuff(test_param)
    self.assertEqual(result, 15)
  
  def test_do_stuff2(self):
    test_param = "sjjs"
    result = script.do_stuff(test_param)
    self.assertIsInstance(result, ValueError)

if __name__ == '__main__':
  unittest.main()
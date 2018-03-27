import unittest
import datetime

class TestpreviousFriday(unittest.TestCase):
  expected_prior_week = datetime.datetime(2018, 3, 16)
  expected_this_week  = datetime.datetime(2018, 3, 23)

  def test_monday(self):
    self.assertEqual(self.expected_prior_week, previousFriday(datetime.datetime(2018, 3, 19)))
  
  def test_tuesday(self):
    self.assertEqual(self.expected_prior_week, previousFriday(datetime.datetime(2018, 3, 20)))
  
  def test_wednesday(self):
    self.assertEqual(self.expected_prior_week, previousFriday(datetime.datetime(2018, 3, 21)))
  
  def test_thursday(self):
    self.assertEqual(self.expected_prior_week, previousFriday(datetime.datetime(2018, 3, 22)))
  
  def test_friday(self):
    self.assertEqual(self.expected_this_week, previousFriday(datetime.datetime(2018, 3, 23)))
  
  def test_saturday(self):
    self.assertEqual(self.expected_this_week, previousFriday(datetime.datetime(2018, 3, 24)))
  
  def test_sunday(self):
    self.assertEqual(self.expected_this_week, previousFriday(datetime.datetime(2018, 3, 25)))

unittest.main()


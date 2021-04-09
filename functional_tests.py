from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # check out this online to-do app homepage
    self.browser.get('http://localhost:8000')

    # notice the page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

if __name__ == '__main__':
  unittest.main()
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title
# assert 'To-Do' in browser.title, "Browser title was " + browser.title

# browser.quit()
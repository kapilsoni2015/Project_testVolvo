#import pytest
import unittest
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class VolvoCarSearch(unittest.TestCase):
	
	def setUp(self):
		#caps = {'browserName': os.getenv('BROWSER', 'chrome')}
		#self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=caps)
		self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
				desired_capabilities=DesiredCapabilities.FIREFOX)

	def test_open_volvoweb(self):
		driver = self.driver
		driver.get("https://www.volvocars.com/intl/v/car-safety/a-million-more")	

	def test_accepting_cookies(self):
		driver = self.driver
		driver.get("https://www.volvocars.com/intl/v/car-safety/a-million-more")
		time.sleep(3)
		driver.find_element_by_css_selector("button[title='Accept']").click()
		time.sleep(2)

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

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
				desired_capabilities=DesiredCapabilities.CHROME)

	def test_open_volvoweb(self):
		driver = self.driver
		driver.get("https://www.volvocars.com/intl/v/car-safety/a-million-more")	

	def test_accepting_cookies(self):
		driver = self.driver
		driver.get("https://www.volvocars.com/intl/v/car-safety/a-million-more")
		time.sleep(3)
		driver.find_element_by_css_selector("button[title='Accept']").click()
		time.sleep(2)

	def test_openelectriccars(self):
		driver = self.driver
		driver.get("https://www.volvocars.com/intl/v/car-safety/a-million-more")
		time.sleep(3)
		driver.find_element_by_css_selector("button[title='Accept']").click()
		time.sleep(3)
		driver.find_element_by_css_selector("._SN-bw._SN-ci._SN-dt._SN-dv._SN-dx._SN-dy._SN-ea._SN-ec._SN-ed._SN-ef._SN-eh._SN-ei._SN-ek._SN-em._SN-gd._SN-gf._SN-gg._SN-gh._SN-gi._SN-gj._SN-gk._SN-hj._SN-hk._SN-hl._SN-hm._SN-i").click()
		driver.find_element_by_css_selector("div[id='vcc-site-nav'] div:nth-child(4) button:nth-child(1) em:nth-child(1)").click()
		time.sleep(2)
		driver.find_element_by_xpath("//em[normalize-space()='Electric cars']").click()
		time.sleep(2)

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

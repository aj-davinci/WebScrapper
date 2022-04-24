from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def createDriver(debug = False):
	options = webdriver.ChromeOptions()

	if not debug:
		options.add_argument('headless')

	options.add_argument('incognito')
	service=Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service, options=options)
	driver.maximize_window()
	driver.delete_all_cookies()
	return driver

import time
from Server import By
from DB import logger
import secrets
from selenium.webdriver.common.action_chains import ActionChains


def nextElement(driver):
	driver.refresh()
	time.sleep(3)

	childLinkElements = driver.find_elements(by=By.XPATH, value="//a[@href]")

	logger("Number of elements found on page: " + str(len(childLinkElements)))

	childLinks = [childLinkElements[i].get_attribute("href") for i in range(len(childLinkElements))]
	childLinks = [childLink for childLink in childLinks if len(childLink) >= 83 and 'Refunds' not in childLink and 'login' not in childLink and 'signup' not in childLink]
	logger("Number of clickable links found on page: " + str(len(childLinks)))


	link = secrets.choice(childLinks)
	logger("Link to be clicked: " + link)

	element = 0
	for childLinkElement in childLinkElements:
		if childLinkElement.get_attribute("href") == link:
			element = childLinkElement

	return element, link


def clickReturn(driver, element):
	actions = ActionChains(driver)
	actions.move_to_element(element).perform()
	time.sleep(3)
	driver.execute_script("arguments[0].click();", element)
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, 120)")
	time.sleep(3)
	driver.back()
	time.sleep(3)
	driver.execute_script("window.scrollTo(0,0)")
	time.sleep(3)
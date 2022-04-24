from Server import createDriver, By, nextElement, clickReturn
from DB import fetchConfig, logger
import time


data = fetchConfig()

for visitor in range(data.visitors):
	driver = createDriver(data.debug)

	driver.get(data.url)
	time.sleep(3)

	for click in range(data.clicks):
		element, link = nextElement(driver)

		if element:
			clickReturn(driver, element)
			logger("Click " + str(click + 1) + " on " + link)
		else:
			logger("No links found on this page")
			driver.quit()

	driver.quit()

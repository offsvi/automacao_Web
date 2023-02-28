from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path = "caminho/para/o/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get("https://www.google.com") 

search_box = driver.find_element_by_css_selector("input[name='q']")
search_box.send_keys("Python automation" + Keys.RETURN)

driver.quit()

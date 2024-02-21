from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://sso.mangatown.com/manga/sakamoto_days/c020/6.html")

element = browser.find_element(By.ID, "image")

response = ActionChains(browser).context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
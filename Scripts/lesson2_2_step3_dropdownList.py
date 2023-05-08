from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "num1")
x = x_element.text
y_element = browser.find_element(By.ID, "num2")
y = y_element.text
summ = int(x) + int(y)

time.sleep(1)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(summ))

time.sleep(1)

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

time.sleep(6)
browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который ищет X и считает y

    x_element = browser.find_element(By.ID, "treasure")
    value_x = x_element.get_attribute("valuex")
    x = value_x
    y = calc(x)
    time.sleep(1)

    # код, который подставляет y в форму

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    time.sleep(1)
    # код, который нажимает чек боксы и радиокнопки

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
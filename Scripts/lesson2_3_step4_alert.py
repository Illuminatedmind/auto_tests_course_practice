from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который жмет кнопку
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    # код, который говорит ок алерту
    confirm = browser.switch_to.alert
    confirm.accept()

    # Ваш код, который ищет X и считает y

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # код, который подставляет y в форму

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
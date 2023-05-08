from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который ждет 100$
    button = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # код, который жмет кнопку
    button = browser.find_element(By.ID, "book")
    button.click()

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
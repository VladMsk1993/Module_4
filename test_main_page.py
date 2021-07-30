import time


def test_guest_see_button_text(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = len(browser.find_elements_by_class_name("btn-primary")) # Измереям найден объект.
    assert button > 0, "I can't find button" # На осовое того, что измерили объект выводим асерт, если значение < 0.
    time.sleep(10)

"""Для запуска тест через комнадную строку, необходимо использовать pytest --language=es test_items.py"""
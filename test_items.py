import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_basket(browser):
    browser.get(link)
    btn = browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(15)
    assert btn, "Явно лишний assert"
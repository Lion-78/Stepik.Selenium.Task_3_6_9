# -*- coding: utf-8 -*-
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
    
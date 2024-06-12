import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])
name = testdata["username"]
password = testdata["password"]
title = testdata["post_title"]
description = testdata["post_description"]
content = testdata["post_content"]

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3)
    text = err_label.text
    site.close()
    time.sleep(testdata["sleep_time"])
    assert text == er1

def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(password)
    btn = site.find_element("css", btn_selector)
    btn.click()
    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    site.close()
    assert text == er2

def test_step3(x_selector1, x_selector2, btn_selector, btn_create,
               title_selector, description_selector, content_selector, btn_savepost, new_post_title, er3):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(password)
    btn1 = site.find_element("css", btn_selector)
    btn1.click()
    btn2 = site.find_element("xpath", btn_create)
    btn2.click()
    time.sleep(testdata["sleep_time"])
    input_title = site.find_element("xpath", title_selector)
    input_title.send_keys(title)
    input_description = site.find_element("xpath", description_selector)
    input_description .send_keys(description)
    input_content = site.find_element("xpath", content_selector)
    input_content.send_keys(content)
    btn3 = site.find_element("xpath", btn_savepost)
    btn3.click()
    time.sleep(testdata["sleep_time"])
    title_label = site.find_element("xpath", new_post_title)
    text = title_label.text
    assert text == er3
    site.close()





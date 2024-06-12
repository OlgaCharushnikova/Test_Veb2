import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
title = testdata["post_title"]
@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""
@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""
@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""
@pytest.fixture()
def title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label"""
@pytest.fixture()
def description_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
@pytest.fixture()
def content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
@pytest.fixture()
def btn_savepost():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
@pytest.fixture()
def btn_create():
    return """//*[@id="create-btn"]"""
@pytest.fixture()
def new_post_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""
@pytest.fixture()
def er2():
    return "Hello, {}".format(name)
@pytest.fixture()
def btn_selector():
    return """button"""
@pytest.fixture()
def er1():
    return "401"
@pytest.fixture()
def er3():
    return "{}".format(title)

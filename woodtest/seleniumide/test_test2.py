# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test2(self):
    self.driver.get("https://uat.mg.kmelearning.com/shyz/shyz/login")
    self.driver.set_window_size(1016, 692)
    self.driver.find_element(By.ID, "account").click()
    self.driver.find_element(By.ID, "account").send_keys("shyz")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Dfcv3344")
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu-open > .ant-menu-submenu-title > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu-active span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu-open > .ant-menu-submenu-title > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu-active > .ant-menu-submenu-title > span").click()
    self.driver.find_element(By.LINK_TEXT, "素材库").click()
    self.driver.find_element(By.LINK_TEXT, "删除").click()
    element = self.driver.find_element(By.LINK_TEXT, "删除")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-sm:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn:nth-child(1)").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("素材名称")
    self.driver.find_element(By.CSS_SELECTOR, "#source .ant-select-selection__rendered").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, "#source svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, "#source svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, "#type .ant-select-selection__rendered").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, "#type .ant-select-selection__rendered").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, "#type .ant-select-selection__rendered").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, "#type .ant-select-selection__rendered").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-form").click()
    self.driver.find_element(By.CSS_SELECTOR, "#type .ant-select-selection__rendered").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, "#type .ant-select-selection__rendered").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-upload > .ant-btn").click()
    self.driver.close()
  

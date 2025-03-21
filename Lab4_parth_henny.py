import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1(self):
        self.driver.get("https://www.calculator.net/bmi-calculator.html")
        self.driver.set_window_size(840, 680)

        # Clear fields before entering values
        age_field = self.driver.find_element(By.ID, "cage")
        age_field.clear()
        age_field.send_keys("43")

        height_field = self.driver.find_element(By.ID, "cheightmeter")
        height_field.clear()
        height_field.send_keys("179")

        weight_field = self.driver.find_element(By.ID, "ckg")
        weight_field.clear()
        weight_field.send_keys("89")

        # Click the calculate button
        self.driver.find_element(By.NAME, "x").click()

        # Wait for the result to be displayed
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bigtext > b"))
        )

        # Assertion to check correct output
        expected_text = "BMI = 27.8 kg/m2"
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".bigtext > b").text.strip()  # Strip spaces
        assert actual_text == expected_text, f"Expected '{expected_text}' but got '{actual_text}'"

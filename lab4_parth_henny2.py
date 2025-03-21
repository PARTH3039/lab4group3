import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBMICalculator:
    def setup_method(self, method):
        """Initialize the WebDriver"""
        self.driver = webdriver.Firefox()  # Change to webdriver.Chrome() if using Chrome
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # Set explicit wait time
        self.vars = {}

    def teardown_method(self, method):
        """Close the WebDriver"""
        self.driver.quit()

    def test_bmi_calculation(self):
        """Test BMI Calculation"""
        self.driver.get("https://www.calculator.net/bmi-calculator.html")

        # Hover over the navigation element
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".topNavAbs > a:nth-child(4)")))
        ActionChains(self.driver).move_to_element(element).perform()

        # Select metric units
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark"))).click()

        # Enter Age
        age_input = self.wait.until(EC.presence_of_element_located((By.ID, "cage")))
        age_input.clear()
        age_input.send_keys("50")

        # Enter Height (cm)
        height_input = self.wait.until(EC.presence_of_element_located((By.ID, "cheightmeter")))
        height_input.clear()
        height_input.send_keys("200")

        # Enter Weight (kg)
        weight_input = self.wait.until(EC.presence_of_element_located((By.ID, "ckg")))
        weight_input.clear()
        weight_input.send_keys("70")

        # Click Calculate Button
        self.wait.until(EC.element_to_be_clickable((By.NAME, "x"))).click()

        # Validate Result
        result = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bigtext > b"))).text
        expected_bmi = "BMI = 17.5 kg/m2"
        assert result == expected_bmi, f"Expected {expected_bmi}, but got {result}"

        print("BMI Calculation Test Passed:", result)

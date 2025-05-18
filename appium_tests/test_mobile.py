from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class MobileAppTest(unittest.TestCase):
    def setUp(self):
        # Appium server capabilities
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11.0',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.example.bugslayer',
            'appActivity': 'com.example.bugslayer.MainActivity',
            'automationName': 'UiAutomator2'
        }
        
        # Initialize the driver
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 10)

    def test_bug_report_creation(self):
        """Test creating a new bug report through mobile app"""
        try:
            # Navigate to bug report screen
            self.driver.find_element(MobileBy.ID, 'create_bug_button').click()
            
            # Fill in bug details
            self.driver.find_element(MobileBy.ID, 'bug_title').send_keys('Mobile Test Bug')
            self.driver.find_element(MobileBy.ID, 'bug_description').send_keys('Bug found during mobile testing')
            
            # Select severity
            self.driver.find_element(MobileBy.ID, 'severity_high').click()
            
            # Submit bug report
            self.driver.find_element(MobileBy.ID, 'submit_bug').click()
            
            # Verify success message
            success_message = self.wait.until(
                EC.presence_of_element_located((MobileBy.ID, 'success_message'))
            )
            self.assertEqual(success_message.text, 'Bug report created successfully')
            
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_test_case_execution(self):
        """Test executing a test case through mobile app"""
        try:
            # Navigate to test cases
            self.driver.find_element(MobileBy.ID, 'test_cases_button').click()
            
            # Select a test case
            self.driver.find_element(MobileBy.ID, 'test_case_1').click()
            
            # Run the test
            self.driver.find_element(MobileBy.ID, 'run_test').click()
            
            # Verify test results
            result = self.wait.until(
                EC.presence_of_element_located((MobileBy.ID, 'test_result'))
            )
            self.assertEqual(result.text, 'Test passed')
            
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main() 
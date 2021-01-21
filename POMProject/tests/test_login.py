from selenium import webdriver
import time
import unittest

from POMProject.pages.loginPage import LoginPage
from POMProject.pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/home/kamini/Documents/Niyuj-assignment/drivers/chromedriver_linux64/chromedriver")

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()


        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

# tearDownClass will run after all testcase run \ testDown will run after every testcase
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if _name_ "" '_main_':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/kamini/Documents/Niyuj-assignment/POMProject/reports')




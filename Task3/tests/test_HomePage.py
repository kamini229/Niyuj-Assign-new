from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time
from Task3.TestData.HomePageData import HomePageData
from Task3.pageObjects.HomePage import HomePage
from Task3.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        time.sleep(5)
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        print(alertText)
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
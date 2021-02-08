import random
import datetime

from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Task2.pages.homepage import Home
from Task2.pages.productspage import Products
import logging

@pytest.mark.usefixtures("OneTimeSetUp")
class TestProductDetailsPage:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='test_execution.log',
                        filemode='w')

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    @pytest.fixture
    def setUp(self):
        logging.debug("Taking screenshot before test execution...")
        self.driver.save_screenshot(
            "/home/kamini/Desktop/Niyuj-Assign-new/Task2/screenshots" +
            str(time.time()).split('.')[0] + ".png")
        yield
        logging.info("Taking screenshot after test execution...")
        self.driver.save_screenshot(
            "/home/kamini/Desktop/Niyuj-Assign-new/Task2/screenshots" +
            str(time.time()).split('.')[0] + ".png")

    def test_website_title(self, setUp):
        home_object = Home(self.driver)
        logging.info("Getting the page title...")
        pageTitle = home_object.getPageTitle()
        logging.info("Comparing the page title with expected title...")
        assert pageTitle == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

    def test_search_functionality(self, setUp):
        home_object = Home(self.driver)
        logging.info("Entering the text into serch box....")
        home_object.enterTextIntoSearchBox("Macbook Pro")
        logging.debug("Clicking on serch icon....")
        home_object.clickSearchIcon()
        product_page = Products(self.driver)
        logging.info("Checking the searched product ...")
        assert product_page.isProductDisplayed() == True

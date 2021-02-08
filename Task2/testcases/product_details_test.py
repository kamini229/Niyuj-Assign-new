import random

from selenium import webdriver
import pytest
import time

from Task2.pages.homepage import Home
from Task2.pages.productdetailspage import ProductDetails
from Task2.pages.productspage import Products


@pytest.mark.usefixtures("OneTimeSetUp")
class TestProductDetailsPage:

    @pytest.fixture
    def setUp(self):
        self.driver.save_screenshot(
            "/home/kamini/Desktop/Niyuj-Assign-new/Task2/screenshots/" +
            str(random.random() * 10000).split('.')[0] + ".png")
        yield
        self.driver.save_screenshot(
            "/home/kamini/Desktop/Niyuj-Assign-new/Task2/screenshots/" +
            str(random.random() * 10000).split('.')[0] + ".png")

    def test_product_title(self, setUp):
        home_object = Home(self.driver)
        home_object.enterTextIntoSearchBox("Macbook pro")
        home_object.clickSearchIcon()
        time.sleep(5)
        parent_window = self.driver.current_window_handle
        print(parent_window)

        product_page = Products(self.driver)
        product_page.clickFirstSearchedProduct()

        time.sleep(3)
        windows_set = self.driver.window_handles
        print(windows_set)

        for window in windows_set:
            if (window != parent_window):
                self.driver.switch_to.window(window)
                self.driver.save_screenshot(
                    "/home/kamini/Desktop/Niyuj-Assign-new/Task2/screenshots/" +
                    str(random.random() * 10000).split('.')[0] + ".png")

        product_detail_object = ProductDetails(self.driver)
        assert product_detail_object.getProductTitle() == "Macbook pro"

    def test_product_price(self, setUp):
        home_object = Home(self.driver)
        home_object.enterTextIntoSearchBox("Macbook pro")
        home_object.clickSearchIcon()
        time.sleep(5)

        parent_window = self.driver.current_window_handle
        print(parent_window)

        product_page = Products(self.driver)
        product_page.clickFirstSearchedProduct()

        time.sleep(3)
        windows_set = self.driver.window_handles
        print(windows_set)

        for window in windows_set:
            if (window != parent_window):
                self.driver.switch_to.window(window)
                self.driver.save_screenshot(
                    "/home/kamini/Desktop/Niyuj-Assign-new/Task2/screenshots/" +
                    str(random.random() * 10000).split('.')[0] + ".png")

        product_detail_object = ProductDetails(self.driver)
        product_price = product_detail_object.getProductPrice()

        assert product_price == "1,27,990.00"



# Source: https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/chapter4.html
"""
This module contains StorePage,
the page object for the AppliFashion store page.
"""
from applitools.selenium import Target, Eyes
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class StorePage:
    BASE_URL = "https://demo.applitools.com/"

    # Locators for elements used during testing
    FILTER_BUTTON = (By.ID, "filterBtn")
    PRODUCT_GRID = (By.ID, "product_grid")

    def __init__(self, driver: WebDriver, page: str):
        self.driver = driver
        self.url = self.BASE_URL + page

    def choose_product(self, selection: str):
        """
        Click on an item in the product grid by finding the product by name.

        :param selection: The position in the grid of the desired product
        """
        product_grid = self.driver.find_element(*self.PRODUCT_GRID)
        product = product_grid.find_element_by_link_text(selection)
        product.click()

    def filter_by(self, label: str):
        """
        Filter the product grid by clicking a checkbox in the filters list.

        :param label: The label of the checkbox to select, partial label is ok
        """
        filter_option = self.driver.find_element(*self.__get_filter_option(label))
        filter_option.click()
        filter_button = self.driver.find_element(*self.FILTER_BUTTON)
        filter_button.click()

    @staticmethod
    def __get_filter_option(label: str) -> tuple:
        """
        Construct the locator for a filter checkbox.

        :param label: Text contained within checkbox ID
        :return: A tuple to locate one or more elements (selenium.webdriver By, locator value)
        """
        return By.XPATH, "//input[contains(@id,'%s')]" % label

    def open(self):
        """
        Open the url of the page (initialized upon instantiation).
        """
        self.driver.get(self.url)

    def visual_check(self, eyes: Eyes, test: str, step: str, region=None):
        """
        Perform a visual check of a page or region.

        :param eyes: Applitools Eyes pytest fixture
        :param test: A name for the test in the batch
        :param step: A name for the step within the test
        :param region: (Optional) A locator tuple (selenium.webdriver By, locator value)
          of a region within the page to capture
        """
        try:
            # Call Open on eyes to initialize a test session
            eyes.open(self.driver, app_name="AppliFashion", test_name=test, viewport_size={"width": 1200, "height": 800})

            # Check the store page with fluent api
            # https://applitools.com/docs/topics/sdk/the-eyes-sdk-check-fluent-api.html
            if region:
                eyes.check(step, Target.region(region=region))
            else:
                eyes.check(step, Target.window().fully().with_name("Store page"))

            # Call Close on eyes to let the server know it should display the results
            eyes.close_async()

        except Exception as e:
            eyes.abort_async()
            print(e)

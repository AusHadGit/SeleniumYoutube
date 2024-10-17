import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from utilities.baseClass import BaseClass
from pageObjects.homePage import HomePage
from selenium.webdriver.common.by import By


class TestChannel(BaseClass):

    def test_channel(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        self.verifyVisibility(homePage.getSearch())
        homePage.getSearch().send_keys("nasa anniversary")
        homePage.getSearchBtn().click()

        time.sleep(10)
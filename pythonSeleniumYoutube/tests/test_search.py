import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from utilities.baseClass import BaseClass
from pageObjects.homePage import HomePage
from pageObjects.videoPage import VideoPage

#remember to run the command with "python -m pytest test_file.py"
class TestSearch(BaseClass):

    def test_search(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        self.verifyVisibility(homePage.getSearch())
        homePage.getSearch().send_keys("nasa")
        homePage.getSearchBtn().click()

        self.verifyVisibility(homePage.getFilter())

        #videoPage = homePage.toVideoPg()
        #self.verifyVisibility(videoPage.getTitle())
        #title = videoPage.getTitle().text.lower()
        #if ("nasa" not in title):
        #    raise Exception('Video title does not have search term')

        time.sleep(10)
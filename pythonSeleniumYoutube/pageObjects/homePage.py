from selenium.webdriver.common.by import By
from pageObjects.videoPage import VideoPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    searchBar = (By.XPATH, "//input[@id='search']")
    searchBtn = (By.XPATH, "//button[@id='search-icon-legacy']")
    homeBtn = (By.XPATH, "//ytd-logo[@class='style-scope ytd-topbar-logo-renderer']")
    actualSearchResult = (By.XPATH, "(//div[@id='title-wrapper'])[2]")
    filterBtn = (By.XPATH, "//div[@id='filter-button']")

    def getSearch(self):
        return self.driver.find_element(*HomePage.searchBar)

    def getSearchBtn(self):
        return self.driver.find_element(*HomePage.searchBtn)

    def getFilter(self):
        return self.driver.find_element(*HomePage.filterBtn)

    def getHomeBtn(self):
        return self.driver.find_element(*HomePage.searchBtn)

    def getResult(self):
        return self.driver.find_element(*HomePage.actualSearchResult)

    def toVideoPg(self):
        videoPage = VideoPage(self.driver)
        return videoPage

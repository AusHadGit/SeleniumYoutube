from selenium.webdriver.common.by import By

class ChannelPage:

    def __init__(self, driver):
        self.driver = driver

    searchBar = (By.XPATH, "//input[@id='search']")
    searchBtn = (By.XPATH, "//button[@id='search-icon-legacy']")
    homeBtn = (By.XPATH, "//ytd-logo[@class='style-scope ytd-topbar-logo-renderer']")
    #For checking the categories available on a Youtube channel, because not all channels have the same amount,
    # we will gather all the category buttons in a list, and search that list for the specific category with get text
    categoryBtn = (By.XPATH, "//div[@class='yt-tab-shape-wiz__tab']")

    #For the subscribe button, this is the address we want, because the value of it can change if we're subscribed or not
    subscribeBtn = (By.XPATH, "//div[@class='yt-flexible-actions-view-model-wiz__action']")


    def getSearch(self):
        return self.driver.find_element(*ChannelPage.searchBar)

    def getSearchBtn(self):
        return self.driver.find_element(*ChannelPage.searchBtn)

    def getHomeBtn(self):
        return self.driver.find_element(*ChannelPage.searchBtn)


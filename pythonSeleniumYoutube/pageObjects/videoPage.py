from selenium.webdriver.common.by import By

class VideoPage:

    def __init__(self, driver):
        self.driver = driver

    searchBar = (By.XPATH, "//input[@id='search']")
    searchBtn = (By.XPATH, "//button[@id='search-icon-legacy']")
    homeBtn = (By.XPATH, "//ytd-logo[@class='style-scope ytd-topbar-logo-renderer']")
    #For checking if a video has been liked or not, check the title value of the address. If it says "I like this", it
    # has already been liked. If liked, it will say "Unlike
    likeBtn = (By.XPATH, "//like-button-view-model[@class='YtLikeButtonViewModelHost']")

    #For the subscribe button, this is the address we want, because the value of it can change if we're subscribed or not
    subscribeBtn = (By.XPATH, "//yt-button-shape[@id='subscribe-button-shape']")

    videoTitle = (By.XPATH, "//div[@id='title']")

    def getSearch(self):
        return self.driver.find_element(*VideoPage.searchBar)

    def getSearchBtn(self):
        return self.driver.find_element(*VideoPage.searchBtn)

    def getHomeBtn(self):
        return self.driver.find_element(*VideoPage.searchBtn)

    def getLikeBtn(self):
        return self.driver.find_element(*VideoPage.likeBtn)

    def getSubBtn(self):
        return self.driver.find_element(*VideoPage.subscribeBtn)

    def getTitle(self):
        return self.driver.find_element(*VideoPage.videoTitle)
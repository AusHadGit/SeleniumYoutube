import inspect
import os
import pytest
import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        # The above line means that when we run the logging, we only run the statements of info level and below
        #logger.debug("A debug statement is executed")
        #logger.info("Information statement")
        #logger.warning("Something is in warning mode")
        #logger.error("A major error has happened")
        #logger.critical("Critical issue")
        return logger

    def verifyVisibility(self, webElement=None):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of(webElement))

    def verifyClickability(self, webElement=None):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(webElement))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def assertionTextCheck(self, word1, text):
        assert word1 in text

    def download_wait(directory, timeout, nfiles=None):
        """Wait for downloads to finish with a specified timeout.

        Args ----
        directory : str
            The path to the folder where the files will be downloaded.
        timeout : int
            How many seconds to wait until timing out.
        nfiles : int, defaults to None
            If provided, also wait for the expected number of files."""

        seconds = 0
        dl_wait = True
        while dl_wait and seconds < timeout:
            time.sleep(1)
            dl_wait = False
            files = os.listdir(directory)
            if nfiles and len(files) != nfiles:
                dl_wait = True

            for fname in files:
                if fname.endswith('.crdownload'):
                    dl_wait = True

            seconds += 1
        return seconds
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://youtube.com")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption("url")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #service_obj = Service("E:\Code Stuff\chromedriver.exe")
        #driver = webdriver.Chrome(options=options, service=service_obj)
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        #service_obj = Service("E:\Code Stuff\geckodriver.exe")
        #driver = webdriver.Firefox(options=options, service=service_obj)
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        #service_obj = Service("E:\Code Stuff\msedgedriver.exe")
        #driver = webdriver.Edge(options=options, service=service_obj)
        driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)

    driver.get(url)

    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.action = action
    yield
    request.cls.driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra

def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
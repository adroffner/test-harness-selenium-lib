""" Selenium Web GUI Test Harness for Python unittest

Use these unittest.TestCase subclasses to run Web GUI tests.
"""

import logging
import unittest

from browser_emulators.chrome.grid_session import ChromeBrowserGridSession
from browser_emulators.firefox.grid_session import FirefoxBrowserGridSession

# log package name.
log = logging.getLogger('.'.join(__name__.split('.')[:-1]))

BROWSER_SESSION_CLASS = {
    'ANDROID': None,
    'CHROME': ChromeBrowserGridSession,
    'EDGE': None,
    'FIREFOX': FirefoxBrowserGridSession,
    'HTMLUNIT': None,
    'HTMLUNITWITHJS': None,
    'INTERNETEXPLORER': None,
    'IPAD': None,
    'IPHONE': None,
    'OPERA': None,
    'PHANTOMJS': None,
    'SAFARI': None,
    'WEBKITGTK': None,
}


class NoBrowserFactoryError(NotImplementedError):
    """ No Browser Factory Error.

    This browser brand has no get_driver() factory class.
    """

    def __init__(self, browser_brand):
        super().__init__(
            'Browser brand "{}" has no Web Driver factory class.'.format(
                browser_brand))


class SeleniumWebGUITestCase(unittest.TestCase):
    """ Selenium Web GUI Test Case.

    This Test Case provides a QA or Regression testing plan.

    This Selenium client describes a Web GUI interface.


    A Selenium Grid service is deployed to emulate browsers already.
    Each test case method should start a browser session and traverse
    its GUI to validate its health.
    """

    # Change these constants in the subclass to set the browser instance.
    GRID_URL = 'http://127.0.0.1:4444/wd/hub'

    BROWSER_BRAND = 'Chrome'  # Chrome, FireFox, ...
    PLATFORM = 'ANY'          # "ANY" or Linux, Windows, ...
    VERSION = None            # Browser version (None means ANY)

    HEADLESS = True
    PAGE_LOAD_TIMEOUT = 20.0  # seconds

    LOG_VERBOSE = True
    LOG_TO_FILE = None

    ACCEPT_SSL_CERTS = False
    HTTP_PROXY_HOST = None
    HTTP_PROXY_PORT = 80

    @classmethod
    def _select_browser_brand_factory(cls, browser_brand):
        """ Select Browser Brand Factory Class.

        :param str browser_brand: match BROWSER_BRAND to its class
        :returns: BrowserGridSession factory or None when not available
        """

        browser_brand = browser_brand.upper()
        browser_factory = BROWSER_SESSION_CLASS.get(browser_brand, None)

        return browser_factory

    @classmethod
    def setUpClass(cls):
        """
        Create a browser factory to get_driver() objects.
        Each browser session has the "desired capabilities" from the constants.
        """

        browser_factory_class = cls._select_browser_brand_factory(cls.BROWSER_BRAND)
        if browser_factory_class is not None:
            cls.browser_factory = browser_factory_class(
                command_executor=cls.GRID_URL,
                platform=cls.PLATFORM,
                browser_version=cls.VERSION,

                headless=cls.HEADLESS,
                page_load_timeout=cls.PAGE_LOAD_TIMEOUT,

                log_verbose=cls.LOG_VERBOSE,
                log_to_file=cls.LOG_TO_FILE,

                accept_ssl_certs=cls.ACCEPT_SSL_CERTS,
                proxy_host=cls.HTTP_PROXY_HOST,
                proxy_port=cls.HTTP_PROXY_PORT,

                raise_errors=True)
        else:
            cls.browser_factory = None

    def setUp(self):
        """ Set Up.

        Create a new browser session "driver" for the current tests.
        """

        super().setUp()
        if self.browser_factory is not None:
            self.driver = self.browser_factory.get_driver()
        else:
            raise NoBrowserFactoryError(self.BROWSER_BRAND)

    def tearDown(self):
        """ Tear Down.

        Quit browser session and release resources.
        """

        super().tearDown()
        if self.driver:
            self.driver.quit()
            self.driver = None

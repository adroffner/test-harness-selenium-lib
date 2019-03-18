""" QA Testing: SeleniumWebGUITestCase Class.

The SeleniumWebGUITestCase is a helper class for QA Testing.
We are testing it here with itself, which is confusing.

Selenium Non-Headless opens a local browser and traverses the UI.
There must be a locally installed Web browser & WebDriver.
A visible GUI shows the events during these QA tests.

The example below demonstrates a Chrome browser session.
    Web Browser: google-chrome-stable
    WebDriver:   chromedriver
"""

from testharness.selenium.testcases import SeleniumWebGUITestCase

from time import sleep


class QAChromeWebGUI(SeleniumWebGUITestCase):
    """ QA Chrome Web GUI.

    Prove that QA tests run with the Chrome Web GUI settings.
    This sets up a visible Firefox Web Driver in a Selenium Local session.
    """

    # Settings: Create Chrome browser with proxy access to the outside.
    BROWSER_BRAND = 'Chrome'
    HEADLESS = False  # Must set False!

    ACCEPT_SSL_CERTS = False
    HTTP_PROXY_HOST = 'one.proxy.att.com'
    HTTP_PROXY_PORT = 8080

    def qa_open_website(self):
        """ Chrome opens a Website.

        Visit SITE_URL and prove the browser went there.
        """

        SITE_URL = 'https://www.python.org/'
        SITE_TITLE = 'Python'  # part of title

        # self.driver is the WebDriver object.
        self.driver.get(SITE_URL)
        sleep(3)

        self.assertEqual(self.driver.current_url, SITE_URL,
                         'Opened Web page: {}'.format(SITE_URL))
        self.assertIn(SITE_TITLE, self.driver.title,
                      'Page Title: "{}"'.format(SITE_TITLE))

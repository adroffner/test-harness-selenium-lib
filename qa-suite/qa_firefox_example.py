""" QA Testing: Firefox Example.

Headless Mode: HEADLESS = True (default)

    Selenium Grid opens a remote browser and traverses the UI.
    There is no visible GUI shown during these QA tests.

Visible Mode: HEADLESS = False

    Selenium Non-Headless opens a local browser and traverses the UI.
    There must be a locally installed Web browser & WebDriver.
    A visible GUI shows the events during these QA tests.

The example below demonstrates a Firefox browser session.
For "Visible Mode", these programs must be installed.
    Web Browser: firefox
    WebDriver:   geckodriver
"""

from testharness.selenium.testcases import SeleniumWebGUITestCase

from time import sleep


class QAFirefoxWebGUI(SeleniumWebGUITestCase):
    """ QA Firefox Web GUI.

    Prove that QA tests run with the Firefox Web GUI settings.
    This sets up a visible Firefox Web Driver in a Selenium Local session.
    """

    GRID_URL = 'http://roattnap03.gcsc.att.com:4444/wd/hub'

    # Settings: Create Firefox browser with proxy access to the outside.
    BROWSER_BRAND = 'Firefox'
    HEADLESS = True

    ACCEPT_SSL_CERTS = False
    HTTP_PROXY_HOST = 'one.proxy.att.com'
    HTTP_PROXY_PORT = 8080

    def qa_open_website(self):
        """ Firefox opens a Website.

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

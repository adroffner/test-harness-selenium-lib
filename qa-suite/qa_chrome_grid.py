""" QA Testing: SeleniumWebGUITestCase Class.

The SeleniumWebGUITestCase is a helper class for QA Testing.
We are testing it here with itself, which is confusing.

Selenium Grid opens a remote browser and traverses the UI.
There is no visible GUI shown during these QA tests.

The example below demonstrates a Chrome browser session.
"""

from testharness.selenium.testcases import SeleniumWebGUITestCase


class QAChromeWebGUI(SeleniumWebGUITestCase):
    """ QA FireFox Web GUI.

    Prove that QA tests run with the Chrome Web GUI settings.
    This sets up a remote Chrome Web Driver in a Selenium Grid.
    """

    GRID_URL = 'http://roattnap04.gcsc.att.com:4444/wd/hub'

    # Settings: Create Chrome browser with proxy access to the outside.
    BROWSER_BRAND = 'Chrome'

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

        self.assertEqual(self.driver.current_url, SITE_URL,
                         'Opened Web page: {}'.format(SITE_URL))
        self.assertIn(SITE_TITLE, self.driver.title,
                      'Page Title: "{}"'.format(SITE_TITLE))

""" SeleniumWebGUITestCase Class Tests.

The SeleniumWebGUITestCase is a helper class for QA Testing.
We are testing it here with itself, which is confusing.
"""

from unittest import mock

from browser_emulators.chrome.grid_session import ChromeBrowserGridSession
from browser_emulators.firefox.grid_session import FirefoxBrowserGridSession

from testharness.selenium.testcases import (
    NoBrowserFactoryError,
    SeleniumWebGUITestCase
)


class DefaultWebGUITests(SeleniumWebGUITestCase):
    """ Default Web GUI Tests.

    Prove that unit tests run the default Web GUI settings.
    This is effectively a Chrome Web Driver.
    """

    # Settings: Defaults

    def setUp(self):
        expected_desired_capabilities = {
            'browserName': 'chrome', 'version': '', 'platform': 'ANY',
            'javascriptEnabled': True, 'acceptSslCerts': False,
            'goog:chromeOptions': {
                'prefs': {
                    'download.default_directory': '/tmp/',
                    'download.directory_upgrade': True,
                    'download.prompt_for_download': False,
                    'safebrowsing.enabled': False,
                    'safebrowsing.disable_download_protection': True
                },
                'extensions': [],
                'args': ['headless', 'no-sandbox', 'window-size=1200x600']
            }
        }

        self.mock_driver = mock.MagicMock()
        with mock.patch('browser_emulators.chrome.grid_session.webdriver.Remote',
                        return_value=self.mock_driver) as mock_webdriver_remote:
            super().setUp()

            mock_webdriver_remote.assert_called_with(
                command_executor=self.GRID_URL,
                desired_capabilities=expected_desired_capabilities)

    def tearDown(self):
        super().tearDown()
        self.mock_driver.quit.assert_called()

    def test_browser_factory_settings(self):
        self.assertIsInstance(self.browser_factory, ChromeBrowserGridSession)

        self.assertEqual(self.browser_factory.command_executor, self.GRID_URL)

        self.assertEqual(self.BROWSER_BRAND.upper(), 'CHROME')
        # self.PLATFORM
        # self.VERSION

        self.assertTrue(self.browser_factory.headless)

        self.assertEqual(self.browser_factory.log_verbose, self.LOG_VERBOSE)
        self.assertEqual(self.browser_factory.log_to_file, self.LOG_TO_FILE)

        # network capabilities.
        self.assertFalse(self.browser_factory.capabilities['acceptSslCerts'])  # self.ACCEPT_SSL_CERTS)
        if self.HTTP_PROXY_HOST is not None:
            self.assertEqual(self.browser_factory.capabilities['httpProxy'],
                             '{}:{}'.format(self.HTTP_PROXY_HOST, self.HTTP_PROXY_PORT))

        # fixed values: always raise WebDriver errors in test cases.
        self.assertEqual(self.browser_factory.download_directory, '/tmp/')
        self.assertTrue(self.browser_factory.raise_errors)

# =========================================================================


class FirefoxWebGUITests(SeleniumWebGUITestCase):
    """ FireFox Web GUI Tests.

    Prove that unit tests run the Firefox Web GUI settings.
    This sets up a remote Firefox Web Driver.
    """

    # Settings: Firefox
    BROWSER_BRAND = 'FIREFOX'

    ACCEPT_SSL_CERTS = True
    HTTP_PROXY_HOST = 'secure.proxy.example.com'
    HTTP_PROXY_PORT = 443

    def setUp(self):
        expected_desired_capabilities = {
            'browserName': 'firefox', 'marionette': True,
            'platform': 'ANY', 'version': None,
            'javascriptEnabled': True,
            'acceptInsecureCerts': True, 'acceptSslCerts': True
        }

        self.mock_driver = mock.MagicMock()
        with mock.patch('browser_emulators.firefox.grid_session.webdriver.Remote',
                        return_value=self.mock_driver) as mock_webdriver_remote:
            super().setUp()

            mock_webdriver_remote.assert_called_with(
                command_executor=self.GRID_URL,
                desired_capabilities=expected_desired_capabilities,
                browser_profile=mock.ANY)

    def tearDown(self):
        super().tearDown()
        self.mock_driver.quit.assert_called()

    def test_browser_factory_settings(self):
        self.assertIsInstance(self.browser_factory, FirefoxBrowserGridSession)

        self.assertEqual(self.browser_factory.command_executor, self.GRID_URL)

        self.assertEqual(self.BROWSER_BRAND.upper(), 'FIREFOX')
        # self.PLATFORM
        # self.VERSION

        self.assertTrue(self.browser_factory.headless)

        self.assertEqual(self.browser_factory.log_verbose, self.LOG_VERBOSE)
        self.assertEqual(self.browser_factory.log_to_file, self.LOG_TO_FILE)

        # network capabilities.
        self.assertTrue(self.browser_factory.capabilities['acceptSslCerts'])
        # NOTE: Firefox Profile objects can't be read for settings?!?

        # fixed values: always raise WebDriver errors in test cases.
        self.assertEqual(self.browser_factory.download_directory, '/tmp/')
        self.assertTrue(self.browser_factory.raise_errors)

# =========================================================================


class NoEdgeWebGUITests(SeleniumWebGUITestCase):
    """ No MS Edge Browser Web GUI Tests.

    Prove that unit tests raise NoBrowserFactoryError.
    """

    # Settings: Missing Browser
    BROWSER_BRAND = 'EDGE'

    def setUp(self):
        with self.assertRaisesRegex(NoBrowserFactoryError, r'^Browser brand "EDGE"'):
            super().setUp()

    def tearDown(self):
        self.assertFalse(hasattr(self, 'driver'))

    def test_no_browser_factory(self):
        """ NoBrowserFactoryError was raised and the "browser_factory" attribute is None """
        self.assertIsNone(self.browser_factory)


class NoInternetExplorerWebGUITests(SeleniumWebGUITestCase):
    """ No MS Internet Explorer Browser Web GUI Tests.

    Prove that unit tests raise NoBrowserFactoryError.
    """

    # Settings: Missing Browser
    BROWSER_BRAND = 'INTERNETEXPLORER'

    def setUp(self):
        with self.assertRaisesRegex(NoBrowserFactoryError, r'^Browser brand "INTERNETEXPLORER"'):
            super().setUp()

    def tearDown(self):
        self.assertFalse(hasattr(self, 'driver'))

    def test_no_browser_factory(self):
        """ NoBrowserFactoryError was raised and the "browser_factory" attribute is None """
        self.assertIsNone(self.browser_factory)


class NoSafariWebGUITests(SeleniumWebGUITestCase):
    """ No Mac Safari Browser Web GUI Tests.

    Prove that unit tests raise NoBrowserFactoryError.
    """

    # Settings: Missing Browser
    BROWSER_BRAND = 'SAFARI'

    def setUp(self):
        with self.assertRaisesRegex(NoBrowserFactoryError, r'^Browser brand "SAFARI"'):
            super().setUp()

    def tearDown(self):
        self.assertFalse(hasattr(self, 'driver'))

    def test_no_browser_factory(self):
        """ NoBrowserFactoryError was raised and the "browser_factory" attribute is None """
        self.assertIsNone(self.browser_factory)

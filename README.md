Selenium Test Harness for Python unittest
=========================================

* [Python and Automated Testing](https://wiki.web.att.com/display/GCSDevOps/Python+and+Automated+Testing)

This **test harness** simplifies automated **Web GUI testing**.
The tests rely on a **Selenium Grid** to provide the browser emulation.

Testing Stages
--------------

This library supports multiple *testing stages*, depending on which **unittest.TestCase** subclass is used.

* **Unit Testing with Mock Services**: The tests do not interact with live services.
* **QA or Regression Testing**: The tests interact with live, fully installed services.

Selenium Python Bindings
------------------------

* [Selenium Python Bindings](https://selenium-python.readthedocs.io/)

The *Test Analyst* must learn to write **Selenium** emulations on a **browser** object.

Development Mode: Visible Browser
---------------------------------

There is a **HEADLESS = False** or _development mode_ that shows a visible Web browser.
By default, **HEADLESS = True** and **Selenium Grid** run the WebDriver session.

Install the **Web browser** and **WebDriver** binaries locally to run this visible browser.
The table below lists some supported Web browsers, and _is subject to change_.

| Browser Brand | Browser Binary (Linux) | WebDriver     |
| ------------- | ---------------------- | ------------- |
| Chrome        | google-chrome-stable   | chromedriver |
| Firefox       | firefox                | geckodriver   |

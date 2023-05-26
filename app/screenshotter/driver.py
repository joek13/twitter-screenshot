from selenium.webdriver import Chrome, ChromeOptions
import os

CHROME_VERSION = os.environ.get("CHROME_VERSION")
DRIVER_VERSION = os.environ.get("DRIVER_VERSION")

if CHROME_VERSION is None:
    assert "CHROME_PATH" in os.environ, "You must either set CHROME_VERSION or set CHROME_PATH explicitly."

if DRIVER_VERSION is None:
    assert "DRIVER_PATH" in os.environ, "You must either set DRIVER_VERSION or set DRIVER_PATH explicitly."

CHROME_PATH = os.environ["CHROME_PATH"] if "CHROME_PATH" in os.environ else f"/opt/chrome/{CHROME_VERSION}/chrome"
DRIVER_PATH = os.environ["DRIVER_PATH"] if "DRIVER_PATH" in os.environ else f"/opt/chromedriver/{DRIVER_VERSION}/chromedriver"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

def get_driver() -> Chrome:
    """Instantiates and configures Selenium WebDriver."""
    options = _get_chrome_options()

    driver = Chrome(executable_path=DRIVER_PATH,
                    options=options,
                    service_log_path='/tmp/chromedriver.log')

    return driver

def _get_chrome_options() -> ChromeOptions:
    chrome_options = ChromeOptions()

    # taken from https://github.com/aws-samples/serverless-ui-testing-using-selenium/blob/main/app.py
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("window-size=3915x2160")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument(f"user-agent={USER_AGENT}")
    chrome_options.binary_location = CHROME_PATH

    return chrome_options
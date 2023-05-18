from pathlib import Path
from . import driver

import re
import time
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
from pathlib import Path

_ZOOM_FACTOR = 1
TWEET_URL_REGEX = re.compile(r"(?:https?://)?twitter\.com/[a-zA-Z_]+/status/\d+", re.MULTILINE)

_HIDE_ELEMENTS_SCRIPT = ""
with open(Path(__file__).resolve().parent.joinpath("hide_elements.js"), "r") as f:
    _HIDE_ELEMENTS_SCRIPT = f.read() # load js to hide ui elements

_IMAGE_CROP_OFFSET = (0, 0, 0, -110) # remove whitespace where ui elements were

browser = driver.get_driver()

def screenshot_tweet(tweet_url: str) -> Image.Image:
    """Screenshots a tweet and returns PIL.Image.
    """
    if not TWEET_URL_REGEX.match(tweet_url):
        tweet_url = "https://twitter.com/" + tweet_url

        if not TWEET_URL_REGEX.match(tweet_url):
            raise ValueError(f"Invalid tweet url {tweet_url}")
    
    browser.get(tweet_url)
    time.sleep(8)

    browser.execute_script(f"document.body.style.zoom='{_ZOOM_FACTOR * 100}%'") # hack to make tweet larger
    # TODO: figure out why this crashes Lambdas
    # browser.execute_script(_HIDE_ELEMENTS_SCRIPT) # hide some ui elements from screenshot

    tweet = browser.find_element(By.TAG_NAME, "article")
    loc = tweet.location
    size = tweet.size

    full_screenshot = browser.get_screenshot_as_png()
    img = Image.open(BytesIO(full_screenshot))

    bounds = (
        _ZOOM_FACTOR * (loc["x"] + _IMAGE_CROP_OFFSET[0]),
        _ZOOM_FACTOR * (loc["y"] + _IMAGE_CROP_OFFSET[1]),
        _ZOOM_FACTOR * (loc["x"] + size["width"] + _IMAGE_CROP_OFFSET[2]),
        _ZOOM_FACTOR * (loc["y"] + size["height"] + _IMAGE_CROP_OFFSET[3])
    )
    cropped = img.crop(bounds)

    browser.close()

    return cropped
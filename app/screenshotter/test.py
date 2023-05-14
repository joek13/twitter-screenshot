from . import driver

if __name__ == "__main__":
    driver = driver.get_driver()
    driver.get("https://news.ycombinator.com")
    driver.save_screenshot("/tmp/screenshot.png")
    driver.close()
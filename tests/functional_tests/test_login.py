"""
Add geckodriver file (https://github.com/mozilla/geckodriver/releases) in /usr/bin
For Linux distr. using Firefox from Snap :
# mkdir $HOME/tmp
# export TMPDIR=$HOME/tmp geckodriver
"""

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By


class TestLogin:
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)

    def teardown_method(self):
        self.driver.close()

    def test_login(self):
        self.driver.get("http://127.0.0.1:5000")
        assert self.driver.current_url == 'http://127.0.0.1:5000/'

        mail_form = self.driver.find_element(By.ID, 'email')
        mail_form.send_keys('john@simplylift.co')
        submit_button = self.driver.find_element(By.TAG_NAME, 'button')
        submit_button.click()

        assert self.driver.current_url == 'http://127.0.0.1:5000/show-summary'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from time import sleep
import chromedriver_autoinstaller

# CONSTANTS:
PROMISED_DL = 150
PROMISED_UL = 10

TWITTER_EMAIL = "****"
TWITTER_PASSWORD = "***"
TWITTER_USERNAME = '***'


class InternetSpeedTwitterBot:
    def __init__(self):
        chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists

        self.driver = webdriver.Chrome()
        self.dl = None
        self.ul = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        # Accept cookies:
        sleep(5)
        accept_cookies = self.get_element('#onetrust-accept-btn-handler', By.CSS_SELECTOR)
        if accept_cookies:
            accept_cookies.click()

        # Start test:
        test_button = self.get_element('a > span.start-text', By.CSS_SELECTOR)
        if test_button:
            test_button.click()
            sleep(60)
        else:
            print("Can;t continue tests!")
            return

        try:
            self.dl = self.get_element('span.download-speed ', By.CSS_SELECTOR).text
            self.ul = self.get_element('span.upload-speed', By.CSS_SELECTOR).text
        except Exception as e:
            print(f"Can't get speeds!\n{e}")
        else:
            print(f"Download speed: {self.dl}")
            print(f"Upload speed: {self.ul}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        self.driver.maximize_window()
        sleep(10)

        # Accept cookies:
        cookies = self.get_element('/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div', By.XPATH)
        if cookies:
            cookies.click()

        # Click login:
        login = self.get_element('/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div', By.XPATH)
        if not login:
            login = self.get_element('/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[1]', By.XPATH)
        if not login:
            login = self.get_element('/html/body/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]', By.XPATH)
        if not login:
            login = self.get_element('/html/body/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]', By.XPATH)

        if not login:
            print("Can't login, Sorry, bye")
        else:
            login.click()

        sleep(5)
        email_field = self.get_element('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input', By.XPATH)
        if not email_field:
            email_field = self.get_element('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input', By.XPATH)
        if not email_field:
            email_field = self.get_element('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input', By.XPATH)

        if not email_field:
            print('Cannot login Bye')
        else:
            email_field.send_keys(TWITTER_EMAIL)
            email_field.send_keys(Keys.ENTER)

        sleep(10)
        pass_field = self.get_element('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input', By.XPATH)
        if not pass_field:
            pass_field = self.get_element('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input', By.XPATH)

        if not pass_field:
            user_field = self.get_element('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input', By.XPATH)
            if user_field:
                user_field.send_keys(TWITTER_USERNAME)
                user_field.send_keys(Keys.ENTER)

            else:
                print("Can't login, Sorry, bye")
                return

        sleep(10)
        pass_field = self.get_element('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input', By.XPATH)
        if not pass_field:
            print("Can't login, Sorry, bye")
            return
        pass_field.send_keys(TWITTER_PASSWORD)
        pass_field.send_keys(Keys.ENTER)

        sleep(10)
        get_started = self.get_element('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/div/a/div', By.XPATH)
        if get_started:
            get_started.click()

        sleep(10)
        tweet = self.get_element('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]', By.XPATH)
        if tweet:
            tweet.click()
            tweet_text = self.get_element('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div', By.XPATH)
            if tweet_text:
                if self.dl and self.ul:
                    tweet_text.send_keys(f'Mój internet Netii ma całkiem niezły transfer - Download: {self.dl} - Uplink: {self.ul}')
                else:
                    print("Nothing to post")
                    print(f"Download speed: {self.dl}")
                    print(f"Upload speed: {self.ul}")
                    return
                sleep(3)
                # Send post
                self.get_element('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]', By.XPATH).click()

    def get_element(self, element, element_type):
        try:
            item = self.driver.find_element(element_type, element)
        except exceptions.NoSuchElementException:
            print(f"Element not found: {element}")
            return None
        else:
            return item

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

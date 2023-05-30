from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from os import path
import os
import time


class Discord:

    isTest = True
    driver = None

    def __init__(self):
        os.environ['WDM_LOG_LEVEL'] = '0'

        options = webdriver.ChromeOptions()
        # Get relative path
        dumps_dir = path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data')
        options.add_argument(r"--user-data-dir=" + dumps_dir)

        options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=options
        )

    def is_logged_in(self):
        self.driver.get("https://discord.com/app")
        current_url = self.driver.current_url
        if current_url == "https://discord.com/login":
            return False

        return True

    def search_users(self):
        time.sleep(5)
        # open "All" list friends
        self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/main/section/div[1]/div[4]/div[2]').click()

        # don't stop deleting
        while True:
            # protection of "Invalid protector"
            try:
                # click on "More" of first user in list
                self.driver.find_elements(By.CLASS_NAME, 'actionButton-3-B2x-')[1].click()
                time.sleep(0.1)
                # click on "Remove friend"
                self.driver.find_element(By.CLASS_NAME, 'colorDanger-3umuSx').click()
                time.sleep(0.1)

                if self.isTest:
                    # click on "Cancel"
                    self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/button[2]').click()
                    time.sleep(2)
                    # print success message we are there
                    print('Test success!')
                    return
                
                # click on "Confirm"
                self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/button[1]').click()
                time.sleep(0.5)
            except:
                # just ignore it
                pass

    def exit(self):
        print("Exiting program...")
        self.driver.quit()

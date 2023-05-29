from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from os import path
import os
import time


class Discord:

    isTest = False
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
        self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/main/section/div[1]/div[4]/div[2]').click()

        # Get user tags
        # users_blocks = self.driver.find_elements(By.CLASS_NAME, 'peopleListItem-u6dGxF')

        # Ask for confirmation
        # print(str(len(users_blocks)) + " users were found")
        # answer = input("Are you sure you want to deleted them? [y/n]\n")
        # if not answer or answer[0].lower() != 'y':
        #     print('You did not indicate approval')
        #     self.exit()

        # Loop through users blocks
        i = 1
        while True:
            try:
                self.driver.find_elements(By.CLASS_NAME, 'actionButton-3-B2x-')[i].click()
                time.sleep(0.1)
                self.driver.find_element(By.CLASS_NAME, 'colorDanger-3umuSx').click()
                time.sleep(0.1)

                # Set isTest variable to test the code
                if self.isTest:
                    self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/button[2]').click()
                else:
                    self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/button[1]').click()

                time.sleep(0.5)
            except:
                pass

    def exit(self):
        print("Exiting program...")
        self.driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

class RobotAmazon:
    def __init__(self, search):
        self.search = search
        self.items = []
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe')



    def pesquisa(self):
        driver = self.driver
        driver.get('https://www.amazon.com.br/')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        user_element.clear()
        user_element.send_keys(self.search)
        user_element.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, window.scrollY + 6000)")

        export_data = driver.find_element_by_class_name('s-main-slot')
        with open('iphone.csv', 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            for row in export_data.find_elements_by_css_selector('div'):
                wr.writerow([d.text for d in row.find_elements_by_css_selector('span')])




amazonRobot = RobotAmazon('Iphone')
amazonRobot.pesquisa()

import time
from selenium import webdriver

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

TARGET_URL = "https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp"

driver.get(TARGET_URL)


class GmailCreator:
    def __init__(self) :
        choice = input("Choose\t:Login or Create Account ")

    def person(self, Fname, Lname, age, DOB,  passwd, phone):

        self.Fname = Fname
        self.Lname = Lname
        self.age = age
        self.DOB = DOB 
        self.passwd = passwd
        self.phone = phone

    def typing_simulator(self, msg):
        msg = [*msg]
        for i in msg:
            time.sleep(1)
            element = driver.find_element(By.NAME, 'identifier')
            element.send.keys(i)
            for i in range(0,2):
                time.sleep(i)

    def page(self,dom_elem='identifier'):
        element = driver.find_element(By.NAME, dom_elem)
        
if __name__ == '__main__':
    info = GmailCreator()
    info.person("William", "Bash",22,"Jan 23, 1967","342yp422wd",12345678)


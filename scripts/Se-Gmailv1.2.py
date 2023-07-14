
import time
from selenium import webdriver

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()

TARGET_URL = "https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp"

driver.get(TARGET_URL)


class GmailCreator:
    #def __init__(self) :
        #choice = input("Choose\t:Login or Create Account ")

    def person(self, Fname, Lname, age, gender, DOB,  passwd, phone):

        self.Fname = Fname
        self.Lname = Lname
        self.age = age
        self.gender = gender
        self.DOB = DOB 
        self.passwd = passwd
        self.phone = phone
        return(Fname, Lname, age,gender,DOB,passwd,phone)

    def typing_simulator(self, msg, attr,classType='' ):
        print('ClassType is : '+classType )
        msg = [*msg]
        for i in msg:
            time.sleep(1)
            if classType == '':

                element = driver.find_element(By.NAME, attr)
                element.send_keys(i)
                for i in range(0,2):
                    time.sleep(i)
                
            elif classType == 'Select':
                element = Select(driver.find_element(By.ID, attr))
                time.sleep(2)
                element.select_by_value('1')
                time.sleep(5)

            if 'phone' in attr:
                element = driver.find_element(By.ID, attr)
                element.send_keys(i)
                for i in range(1,2):
                    time.sleep(i)


    def reg_fields(self, personal_info):
        print(personal_info) 
        #fields = ['firstName','lastName','month', 'gender','Selectionc0','Passwd', 'PasswdAgain','phoneNumberId']
        fields = ['Name','month', 'gender','Selectionc0','Passwd','phoneNumberId']
            
        
#        variables = [Fname, Lname, month,day,year, gender,passwd, phone ]
        
        for x in fields:
            descr = x 
            print(descr)
            
            if 'Name' in x:

                self.typing_simulator(self.Fname, 'firstName')
                self.typing_simulator(self.Lname, 'lastName')

                button = driver.find_element(By.TAG_NAME, 'button')
                button.click()
                time.sleep(5)
                #self.buttonClick()
                print("Buttons aftermath do you read#1")



               
            elif 'Passwd' in x:
                print('inside Passwd condition')
                password = driver.find_element(By.NAME, 'Passwd')
                self.typing_simulator(self.passwd, 'Passwd')
                time.sleep(1)
                self.typing_simulator(self.passwd, 'PasswdAgain')
                time.sleep(1)
                self.buttonClick()
            


                print("this is the password condition"+self.passwd)
                print(self.passwd+'for the second time confimations :')

            elif 'month' in x:
                print('month condition')
                self.birthday()
                
            elif 'gender' in x:
                print('gender condition')
                #self.typing_simulator("1", 'gender',classType="Selector")

                gender = Select(driver.find_element(By.ID, 'gender'))
                gender.select_by_visible_text('Female')
            
            
                self.buttonClick()
                time.sleep(5)
            
            elif 'Select' in x:
                email = driver.find_element(By.ID, 'selectionc0').click()
                self.buttonClick()
                time.sleep(5)
            
            elif 'phone' in x:
                print("phone condition\nThis should pipe into reverse ssh and into client phone to grab sms code data")
                self.typing_simulator(self.phone, 'phoneNumberId', classType = "other")
                time.sleep(5)
                self.buttonClick()
            








    def buttonClick(self):
        button = driver.find_element(By.TAG_NAME, 'button')
        button.click()

    def birthday(self):
        month = Select(driver.find_element(By.ID, 'month'))
        month.select_by_visible_text("January")
        time.sleep(2)
        day = driver.find_element(By.ID, 'day')
        day.send_keys('23')
        time.sleep(5)
        self.typing_simulator('2008', 'year')
        


if __name__ == '__main__':
    gmail = GmailCreator()
    personal_info = gmail.person("William", "Bash",22,'female', "Jan 23 1964","*342yp!422wd#",'1234567')
    gmail.reg_fields(personal_info)



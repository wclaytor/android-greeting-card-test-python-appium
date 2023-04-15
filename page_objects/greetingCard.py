from selenium.webdriver.common.by import By
from .common import CommonOps

class GreetingCard(CommonOps):

    # elements
    greeting = (By.XPATH, "//android.widget.TextView")

    def verifyGreeting(self):
        self.wait_for(self.greeting)
        assert self.find(self.greeting).text == "Hi, my name is Android!"
        


import logging

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
)

from page_objects.greetingCard import GreetingCard

scenarios('../../features/greeting.feature')

@given('user is on card page')
def _(driver):
    logging.info("card page is visible")

@when('user views the greeting')
def _(driver):
    logging.info("greeting is viewed")

@then('user should see "Hi, my name is wclaytor!"')
def _(driver):
    #assertion happen here
    GreetingCard(driver).verifyGreeting()
    logging.info("login page is visible")


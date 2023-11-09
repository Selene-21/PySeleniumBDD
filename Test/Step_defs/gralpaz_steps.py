from pytest_bdd import scenarios, then, parsers, when
from selenium.webdriver.common.by import By
from Pages.GralPazpages import gralpazhome

#Scenarios
scenarios('../Features/GralPaz.feature')

@when(parsers.parse('realiza un click en "mail_address"'))
def check_mail_address(browser, mail_address):
    gralpaz_home = gralpazhome(browser)
    assert gralpaz_home.get_mail_address().click() in mail_address


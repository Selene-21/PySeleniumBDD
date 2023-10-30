from pytest_bdd import scenarios, then, parsers
from selenium.webdriver.common.by import By
from Pages.GralPazpages import gralpazhome

#Scenarios
scenarios('../Features/GralPaz.feature')

@when(parsers.parse(''))

@then(parsers.parse(''))
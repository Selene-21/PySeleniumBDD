from pytest_bdd import scenarios, then, parsers
from selenium.webdriver.common.by import By
from Pages.yvytupages import yvytuhome

#Scenarios
scenarios('../Features/Yvytu.feature')

@then(parsers.parse('el titulo principal es "{main_title}"'))
def check_main_title(browser, main_title):
    yvytu_home = Yvytupage(browser)
    assert yvytu_home.get_main_title().txt in main_title print("Se verifico el titulo"+main_title).text
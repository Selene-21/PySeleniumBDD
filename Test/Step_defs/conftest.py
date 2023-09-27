import pytest
from pytest_bdd import given, parsers
from selenium import webdriver


YVYTU_HOME = "https://vientosdelaselva.com.ar/"
CLARO_HOME = ""
EDEN_HOME = ""
OBERLY_HOME = ""

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
    
@given(parsers.parse('que un usuario esta en la pagina de "{web_Name}"'))
def go_home_page(browser, web_Name):
    if web_Name == "Yvytu":
        browser.get(YVYTU_HOME)
    elif web_Name == "Tienda":
        browser.get(CLARO_HOME)
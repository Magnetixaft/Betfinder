from selenium import webdriver
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
team_one = ("Inter")
team_two = ("Fiorentina")

firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('window-size=1920x1080')

driver_path = ("c:/Users/Johan/Webdrivers/geckodriver")
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)
CSS = driver.find_element_by_css_selector

URL = ('https://www.unibet.se/betting/sports/home')
driver.get(URL)
print(driver.title)
driver.implicitly_wait(2)
search_click = CSS('button.c2fe3')
search_click.click()
search_bar = CSS('.d647b')
search_bar.send_keys(team_one)

try:
    search_search_first = CSS("._358d9 > a:nth-child(2)")
except Exception:
    pass
try:
    search_search_second = CSS("._358d9 > a:nth-child(3)")
except Exception:
    pass
try:
    search_search_third = CSS("._358d9 > a:nth-child(4)")
except Exception:
    pass
try:
    search_search_fourth = CSS("._358d9 > a:nth-child(5)")
except Exception:
    pass
driver.implicitly_wait(2)
try:

    if ("Fotboll") in search_search_first.text:
        length_of_word1 = CSS('div._358d9:nth-child(1) > a:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
        if (len(length_of_word1.text) > (len(team_one))):
            pass
        else: search_search_first.click()
except Exception:
    pass
try:
    if ("Fotboll") in search_search_second.text:
        length_of_word2 = CSS('div._358d9:nth-child(1) > a:nth-child(3) > div:nth-child(1) > span:nth-child(1)')
        if (len(length_of_word2.text) > (len(team_one))):
            pass
        else: search_search_second.click()
except Exception:
    pass
try:
    if ("Fotboll") in search_search_third.text:
        length_of_word3 = CSS('div._358d9: nth - child(1) > a:nth - child(4) > div: nth - child(1) > span:nth - child(1)')
        if (len(length_of_word2.text) > (len(team_one))):
            pass
        else: search_search_third.click()
except Exception:
    pass
try:
    if ("Fotboll") in search_search_fourth.text:
        length_of_word4 = CSS('._358d9 > a:nth-child(5) > div:nth-child(1) > span:nth-child(1)')
        if (len(length_of_word4.text) > (len(team_one))):
            pass
        else: search_search_fourth.click()
except Exception:
    pass

first_result = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
second_result = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
driver.implicitly_wait(1)
if (team_two) in first_result.text:
    Odds11 = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1)')
    Tie = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
    Odds12 = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1)')
    if (team_one) in Odds11.text:
        Odds_team_one = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        Odds_team_two = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        print(team_one, ": ", Odds_team_one.text)
        print("Tie: ", Tie.text)
        print(team_two, ": ", Odds_team_two.text)
    elif (team_one) in Odds12.text:
        Odds_team_one = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        Odds_team_two = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        print(team_one, ": ", Odds_team_one.text)
        print("Tie: ", Tie.text)
        print(team_two, ": ", Odds_team_two.text)

if (team_two) in second_result.text:
    Odds21 = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1)')
    Tie = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
    Odds22 = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1)')
    if (team_one) in Odds21.text:
        Odds_team_one = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        Odds_team_two = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        print(team_one, ": ", Odds_team_one.text)
        print("Tie: ", Tie.text)
        print(team_two, ": ", Odds_team_two.text)
    elif (team_one) in Odds22.text:
        Odds_team_one = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        Odds_team_two = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        print(team_one, ": ", Odds_team_one.text)
        print("Tie: ", Tie.text)
        print(team_two, ": ", Odds_team_two.text)
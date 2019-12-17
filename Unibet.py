from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
firefox_options = Options()


firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('window-size=1920x1080')

driver_path = ("c:/Users/Johan/Webdrivers/geckodriver")
driver = webdriver.Firefox(executable_path=driver_path)#, options=firefox_options)

team_one = ("Everton")
team_two = ("Arsenal")
def Unibet_main():

    CSS = driver.find_element_by_css_selector
    URL = ('https://www.unibet.se/betting/sports/home')
    driver.get(URL)
    driver.implicitly_wait(1)
    search_click = CSS('button.c2fe3')
    search_click.click()
    search_bar = CSS('.d647b')
#dropdown menyn kommer inte alltid upp, detta sinkar allt men måste användas
    def Search():
        driver.implicitly_wait(1)
        search_bar.clear()
        search_bar.send_keys(team_one)
        driver.implicitly_wait(2)

        #search_bar.send_keys(team_one[-1])
        try:
            CSS('._0453d')
        except NoSuchElementException:
            search_bar.send_keys(Keys.BACKSPACE)
            driver.implicitly_wait(2)
            try:
                CSS('._0453d')
            except NoSuchElementException:
                Search()
            else:
                pass
        else:
            pass
    Search()

#alla sporter och andra lag kommer upp, detta söker efter rätt sport och lag som bara har samma antal karaktärer som laget
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
    try:
        search_search_fifth = CSS("._358d9 > a:nth-child(6)")
    except Exception:
        pass
    try:
        if ("Fotboll") in search_search_first.text:
            length_of_word1 = CSS('._358d9 > a:nth-child(2) > div:nth-child(1)')
            if (len(length_of_word1.text) > (len(team_one))):
                pass
            else: search_search_first.click()
    except Exception:
        pass
    try:
        if ("Fotboll") in search_search_second.text:
            length_of_word2 = CSS('._358d9 > a:nth-child(3) > div:nth-child(1)')
            if (len(length_of_word2.text) > (len(team_one))):
                pass
            else: search_search_second.click()
    except Exception:
        pass
    try:
        if ("Fotboll") in search_search_third.text:
            length_of_word3 = CSS('._358d9 > a:nth-child(4) > div:nth-child(1)')
            if (len(length_of_word3.text) > (len(team_one))):
                pass
            else: search_search_third.click()
    except Exception:
        pass
    try:
        if ("Fotboll") in search_search_fourth.text:
            length_of_word4 = CSS('._358d9 > a:nth-child(5) > div:nth-child(1)')
            if (len(length_of_word4.text) > (len(team_one))):
                pass
            else: search_search_fourth.click()
    except Exception:
        pass
    try:
        if ("Fotboll") in search_search_fifth.text:
            length_of_word5 = CSS('._358d9 > a:nth-child(5) > div:nth-child(1)')
            if (len(length_of_word5.text) > (len(team_one))):
                pass
            else: search_search_fourth.click()
    except Exception:
        pass

    def loaded_failed():
        loaded_attempts = 0
        if loaded_attempts < 5:
            loaded_attempts += 1

            try:
                driver.implicitly_wait(1)
                CSS('.KambiBC-event-item-1005561154 > a:nth-child(1) > div:nth-child(1)')
            except NoSuchElementException:

                driver.refresh()
                loaded_failed()
            else:
                pass
            return loaded_attempts
        else:
            driver.quit()
            Unibet_main()
    loaded_failed()

    first_result = CSS('.KambiBC-event-item-1005561154 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    second_result = CSS('li.KambiBC-event-item:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    time.sleep(1)
#Sorterar om lag ett är val 1 eller 2
    if (team_two) in first_result.text:
        Odds11 = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1)')
        Tie = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
        Odds12 = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1)')
        if (team_one) in Odds11.text:
            Odds_team_one = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
            Odds_team_two = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
            print("Unibet:")
            print(team_one, ": ", Odds_team_one.text)
            print("Tie: ", Tie.text)
            print(team_two, ": ", Odds_team_two.text)
        elif (team_one) in Odds12.text:
            Odds_team_one = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
            Odds_team_two = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
            print("Unibet:")
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
            print("Unibet:")
            print(team_one, ": ", Odds_team_one.text)
            print("Tie: ", Tie.text)
            print(team_two, ": ", Odds_team_two.text)
        elif (team_one) in Odds22.text:
            Odds_team_one = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
            Odds_team_two = CSS('div.KambiBC-collapsible-container:nth-child(3) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
            print("Unibet:")
            print(team_one, ": ", Odds_team_one.text)
            print("Tie: ", Tie.text)
            print(team_two, ": ", Odds_team_two.text)

